from __future__ import annotations
from collections import defaultdict

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

    def deduplicate_input_socket_names(node_obj: Node):
        """
        Deduplicates input socket names by appending a number if necessary.
        """
        name_counts: defaultdict[str, int] = defaultdict(int)
        for input_socket in node_obj.input_sockets:
            name_counts[input_socket.name] += 1

        needs_deduplication = set()
        for input_socket in node_obj.input_sockets:
            if name_counts[input_socket.name] > 1:
                needs_deduplication.add(input_socket.name)

        for input_socket in reversed(node_obj.input_sockets):
            if input_socket.name not in needs_deduplication:
                continue

            original_name = input_socket.name
            input_socket.name = f"{original_name}_{name_counts[original_name]}"
            name_counts[original_name] -= 1

    add_property_input_sockets()
    add_node_input_sockets()
    add_output_sockets()
    deduplicate_input_socket_names(node_obj)
    return node_obj


# Track how many times each (node, socket base) pair has been linked
_find_link_sockets_counters: dict[tuple[str, str], int] = {}


def find_link_sockets(
    node_system: NodeSystem, blender_link
) -> tuple[Optional[InputSocket], Optional[OutputSocket]]:
    """
    Given a node system and a blender link, find the corresponding input socket and source output socket.
    Handles deduplicated input sockets (e.g., Shader_1, Shader_2) for duplicate Blender socket names.
    Returns (input_socket, source_socket) or (None, None) if not found.
    """
    to_node_name = to_python_identifier(blender_link.to_node.name)
    to_socket_base = to_python_identifier(blender_link.to_socket.name)
    from_node_name = to_python_identifier(blender_link.from_node.name)
    from_socket_name = to_python_identifier(blender_link.from_socket.name)

    # Find the target node
    for node in node_system.nodes:
        if node.name != to_node_name:
            continue
        # Gather all input sockets that match the base name or deduplicated name
        matching_sockets = [
            s
            for s in node.input_sockets
            if s.name == to_socket_base
            or (
                s.name.startswith(f"{to_socket_base}_")
                and s.name[len(to_socket_base) + 1 :].isdigit()
            )
        ]

        # Sort so that base comes first, then _1, _2, ...
        def socket_sort_key(s):
            if s.name == to_socket_base:
                return 0
            try:
                return int(s.name[len(to_socket_base) + 1 :])
            except Exception:
                return 9999

        matching_sockets.sort(key=socket_sort_key)
        # Use a counter to pick the next available deduplicated socket for this node/socket base
        counter_key = (node.name, to_socket_base)
        idx = _find_link_sockets_counters.get(counter_key, 0)
        if idx < len(matching_sockets):
            input_socket = matching_sockets[idx]
            _find_link_sockets_counters[counter_key] = idx + 1
        else:
            input_socket = None
        # Find the source node and output socket
        source_node = next(
            (n for n in node_system.nodes if n.name == from_node_name), None
        )
        source_socket = None
        if source_node is not None:
            source_socket = next(
                (s for s in source_node.output_sockets if s.name == from_socket_name),
                None,
            )
        return input_socket, source_socket
    return None, None


def convert_from_blender(blender_nodes: bpy.types.NodeTree) -> NodeSystem:
    node_system = NodeSystem()

    for blender_node in blender_nodes.nodes:
        node_obj = create_node_from_blender_node(blender_node)
        node_system.add_node(node_obj)

    # Set sources for input sockets
    for blender_link in blender_nodes.links:
        assert blender_link.to_socket is not None
        assert blender_link.to_node is not None
        assert blender_link.from_socket is not None
        assert blender_link.from_node is not None

        input_socket, source_socket = find_link_sockets(node_system, blender_link)
        if input_socket is not None and source_socket is not None:
            input_socket.source = source_socket
        else:
            print(
                f"[WARNING] Could not link: {blender_link.from_node.name}.{blender_link.from_socket.name} -> "
                f"{blender_link.to_node.name}.{blender_link.to_socket.name}"
            )

    return node_system
