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

    # Arrange nodes in a topological order
    x_offset = 200
    for index, node_system_node in enumerate(node_system.get_nodes_topologically()):
        blender_node = blender_nodes[node_system_node.name]

        blender_node.location = (
            x_offset * index,
            0,
        )

    return material
