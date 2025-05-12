from __future__ import annotations

import bpy
from .node_system import NodeSystem, Node
from .blender_nodes_layout import layout_blender_nodes


def get_blender_input_name(input_socket_name: str) -> str:
    """
    Maps names like 'Shader_1', 'Shader_2' to Blender's 'Shader', 'Shader_001', etc.
    """
    import re

    m = re.match(r"(.+?)_(\d+)$", input_socket_name)
    if not m:
        return input_socket_name

    base_name, idx = m.group(1), int(m.group(2))
    if idx == 1:
        return base_name

    return f"{base_name}_{idx - 1:03d}"


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
            apply_input_socket_to_blender_node(blender_node, input_socket)

    # Create links between nodes
    for node_system_node in node_system.nodes:
        if not isinstance(node_system_node, Node):
            continue

        for input_socket in node_system_node.input_sockets:
            if input_socket.source:
                from_node = blender_nodes[input_socket.source.node.name]
                from_socket = from_node.outputs[input_socket.source.name]
                to_node = blender_nodes[node_system_node.name]
                blender_input_name = get_blender_input_name(input_socket.name)
                to_socket = to_node.inputs[blender_input_name]
                node_tree.links.new(from_socket, to_socket)

    # Arrange nodes in a left-to-right flow based on their level in the graph
    layout_blender_nodes(node_system, blender_nodes)

    return material


def normalize_name(name: str) -> str:
    """
    Normalize a Blender socket name to Node Code style:
    - Replace spaces with underscores
    - Remove trailing/leading whitespace
    - Keep acronyms (all-uppercase words) as is
    """
    # Remove leading/trailing whitespace
    name = name.strip()
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    return name


def apply_input_socket_to_blender_node(blender_node, input_socket) -> None:
    """
    Applies an InputSocket to a Blender node, setting the appropriate property or input value.
    Normalizes Blender socket names to Node Code style for robust mapping.
    """
    # Use get_blender_input_name to map NodeCode input name to Blender's input name
    blender_input_name = get_blender_input_name(input_socket.name)
    blender_input_map = {normalize_name(inp.name): inp for inp in blender_node.inputs}
    blender_input = blender_input_map.get(normalize_name(blender_input_name))
    if blender_input:
        if not hasattr(blender_input, "default_value"):
            print(
                f"Warning: Blender input '{blender_input.name}' on node '{getattr(blender_node, 'bl_idname', type(blender_node).__name__)}' does not have a 'default_value' attribute."
            )
            return
        blender_input.default_value = input_socket.value
        return

    # Fallback: try property on the node
    if not hasattr(blender_node, input_socket.name):
        print(
            f"Warning: Blender object {getattr(blender_node, 'bl_idname', type(blender_node).__name__)} has neither input socket nor property matching Node Code input {input_socket.name}={input_socket.value}"
        )
        return

    try:
        # Blender node property
        setattr(blender_node, input_socket.name, input_socket.value)
        return
    except AttributeError:
        print(
            f"Warning: Failed to set Blender object {getattr(blender_node, 'bl_idname', type(blender_node).__name__)} property {input_socket.name}={input_socket.value}."
        )
        return
