# Required by Python 3.13 for Python to ignore type hints at runtime.
# Without this, running "tox" fails with annotation typing errors.
from __future__ import annotations

import bpy
from .node_system import NodeSystem, Node, InputSocket, OutputSocket
from .utils import should_ignore_property
from typing import Any, Optional


def to_python_datatype(value: Optional[bpy.types.Property]) -> Any:
    """
    Converts a Blender property value to a Python datatype.
    """
    if value is None:
        return None

    if "bpy" not in str(type(value)):
        # Already a Python type
        return value

    if isinstance(value, bpy.types.bpy_prop_array):
        return tuple([to_python_datatype(v) for v in value])

    raise ValueError(
        f"Unsupported property type: {type(value)} for {value}. Please implement a conversion for this type."
    )


def convert_from_blender(blender_nodes: bpy.types.NodeTree) -> NodeSystem:
    node_system = NodeSystem()

    for blender_node in blender_nodes.nodes:
        # Create a Node object
        node_type = blender_node.bl_idname
        node_type = node_type.replace("ShaderNode", "")
        node_obj = Node(name=blender_node.name, node_type=node_type)

        # Add input sockets for properties
        for prop_id, prop in blender_node.bl_rna.properties.items():
            if should_ignore_property(prop_id, prop):
                continue

            input_socket_obj = InputSocket(
                name=prop_id,
                node=node_obj,
                value=to_python_datatype(getattr(blender_node, prop_id, None)),
                source=None,
            )
            node_obj.add_input_socket(input_socket_obj)

        # Add input sockets for node inputs
        for blender_input_socket in blender_node.inputs:
            input_socket_obj = InputSocket(
                name=blender_input_socket.name,
                node=node_obj,
                value=to_python_datatype(blender_input_socket.default_value)
                if hasattr(blender_input_socket, "default_value")
                else None,
                source=None,  # Source will be set later if connected
            )
            node_obj.add_input_socket(input_socket_obj)

        # Fixed redefinition error by renaming the variable
        for output_socket in blender_node.outputs:
            output_socket_obj: OutputSocket = OutputSocket(
                name=output_socket.name, node=node_obj
            )
            node_obj.add_output_socket(output_socket_obj)

        # Add the node to the NodeSystem
        node_system.add_node(node_obj)

    # Set sources for input sockets
    for node in node_system.nodes:
        for input_socket in node.input_sockets:
            for link in blender_nodes.links:
                assert link.to_socket is not None
                assert link.to_node is not None
                assert link.from_socket is not None
                assert link.from_node is not None
                if (
                    link.to_socket.name == input_socket.name
                    and link.to_node.name == node.name
                ):
                    source_node = next(
                        n for n in node_system.nodes if n.name == link.from_node.name
                    )
                    source_socket = next(
                        s
                        for s in source_node.output_sockets
                        if s.name == link.from_socket.name
                    )
                    input_socket.source = source_socket

    return node_system


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

        # Set input properties
        for input_socket in node_system_node.input_sockets:
            if hasattr(blender_node, input_socket.name):
                setattr(blender_node, input_socket.name, input_socket.value)
            else:
                print(
                    f"Warning: Node Code property {input_socket.name} not found in Blender object {blender_node.bl_idname}"
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
