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


def to_python_identifier(name: str) -> str:
    """
    Converts a Blender property name to a Python identifier.
    """
    # Remove any special characters and replace spaces with underscores
    return name.replace(" ", "_").replace("-", "_").replace(".", "_").replace(",", "_")


def create_node_from_blender_node(blender_node: bpy.types.Node) -> Node:
    """
    Converts a Blender node to a NodeSystem Node (without links).
    """
    node_type = blender_node.bl_idname.replace("ShaderNode", "")
    node_obj = Node(name=to_python_identifier(blender_node.name), node_type=node_type)

    def add_property_input_sockets():
        for prop_id, prop in blender_node.bl_rna.properties.items():
            if should_ignore_property(prop_id, prop):
                continue
            input_socket_obj = InputSocket(
                name=to_python_identifier(prop_id),
                node=node_obj,
                value=to_python_datatype(getattr(blender_node, prop_id, None)),
                source=None,
            )
            node_obj.add_input_socket(input_socket_obj)

    def add_node_input_sockets():
        for blender_input_socket in blender_node.inputs:
            input_socket_obj = InputSocket(
                name=to_python_identifier(blender_input_socket.name),
                node=node_obj,
                value=to_python_datatype(blender_input_socket.default_value)
                if hasattr(blender_input_socket, "default_value")
                else None,
                source=None,
            )
            node_obj.add_input_socket(input_socket_obj)

    def add_output_sockets():
        for output_socket in blender_node.outputs:
            output_socket_obj = OutputSocket(
                name=to_python_identifier(output_socket.name), node=node_obj
            )
            node_obj.add_output_socket(output_socket_obj)

    add_property_input_sockets()
    add_node_input_sockets()
    add_output_sockets()
    return node_obj


def convert_from_blender(blender_nodes: bpy.types.NodeTree) -> NodeSystem:
    node_system = NodeSystem()

    for blender_node in blender_nodes.nodes:
        node_obj = create_node_from_blender_node(blender_node)
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
                    to_python_identifier(link.to_socket.name) == input_socket.name
                    and to_python_identifier(link.to_node.name) == node.name
                ):
                    source_node = next(
                        n
                        for n in node_system.nodes
                        if n.name == to_python_identifier(link.from_node.name)
                    )
                    source_socket = next(
                        s
                        for s in source_node.output_sockets
                        if s.name == to_python_identifier(link.from_socket.name)
                    )
                    input_socket.source = source_socket

    return node_system
