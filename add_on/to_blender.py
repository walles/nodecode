from __future__ import annotations

import bpy
from .node_system import NodeSystem, Node


def create_blender_material(node_system: NodeSystem) -> bpy.types.Material:
    """
    Converts a NodeSystem into a new Blender material.
    """
    # Create a new material
    material = bpy.data.materials.new(name="NodeCodeMaterial")
    material.use_nodes = True

    # Get the node tree of the material
    node_tree = material.node_tree
    if node_tree is None:
        raise ValueError("Material node tree is None. Cannot proceed with conversion.")

    # Clear existing nodes
    for node in list(node_tree.nodes):
        node_tree.nodes.remove(node)

    # Create a mapping of NodeSystem node names to Blender nodes
    blender_nodes: dict[str, bpy.types.Node] = {}
    for node_system_node in node_system.nodes:
        blender_node = node_tree.nodes.new(
            type=f"ShaderNode{node_system_node.node_type}"
        )
        blender_node.name = node_system_node.name
        blender_nodes[node_system_node.name] = blender_node

        # Set input sockets and properties with type checking
        for input_socket in node_system_node.input_sockets:
            blender_input = blender_node.inputs.get(input_socket.name)
            if blender_input and hasattr(blender_input, "default_value"):
                blender_input.default_value = input_socket.value
            elif hasattr(blender_node, input_socket.name):
                try:
                    setattr(blender_node, input_socket.name, input_socket.value)
                except AttributeError:
                    print(
                        f"Warning: Node Code property {input_socket.name}={input_socket.value} not found or not settable in Blender object {blender_node.bl_idname}"
                    )
            else:
                print(
                    f"Warning: Node Code property {input_socket.name}={input_socket.value} not found or not settable in Blender object {blender_node.bl_idname}"
                )

    # Create links between nodes
    for node_system_node in node_system.nodes:
        if not isinstance(node_system_node, Node):
            continue

        for input_socket in node_system_node.input_sockets:
            if input_socket.source:
                from_node = blender_nodes[input_socket.source.node.name]
                from_socket = from_node.outputs[input_socket.source.name]
                to_node = blender_nodes[node_system_node.name]
                to_socket = to_node.inputs[input_socket.name]
                node_tree.links.new(from_socket, to_socket)

    # Arrange nodes in a left-to-right flow based on their level in the graph
    def get_node_levels(node_system):
        levels: dict[str, int] = {}

        def visit(node, level):
            if node.name in levels:
                levels[node.name] = max(levels[node.name], level)
            else:
                levels[node.name] = level
            for out in getattr(node, "output_sockets", []):
                for target in getattr(out, "targets", []):
                    visit(target.node, level + 1)

        for node in node_system.nodes:
            if all(not inp.source for inp in getattr(node, "input_sockets", [])):
                visit(node, 0)
        # Ensure all nodes are included, even if not reached in traversal (e.g., pure sink nodes)
        for node in node_system.nodes:
            if node.name not in levels:
                # Level is one higher than the max level of its input sources, or 0 if no sources
                input_levels = [
                    levels.get(inp.source.node.name, 0)
                    for inp in getattr(node, "input_sockets", [])
                    if inp.source
                ]
                levels[node.name] = max(input_levels, default=0) + 1
        return levels

    levels = get_node_levels(node_system)
    x_offset = 300

    # Group nodes by level
    level_nodes: dict[int, list[str]] = {}
    for node_name, level in levels.items():
        level_nodes.setdefault(level, []).append(node_name)
    # Assign Y positions: nodes at the same level are stacked vertically, X by level
    y_offset = 200
    for level, nodes in level_nodes.items():
        for i, node_name in enumerate(sorted(nodes)):
            blender_node = blender_nodes[node_name]
            blender_node.location = (
                x_offset * level,
                -y_offset * i,  # Stack nodes at the same level vertically
            )

    return material
