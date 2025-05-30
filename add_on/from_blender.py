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

    # Handle Blender Color type by attribute presence
    if hasattr(value, "r") and hasattr(value, "g") and hasattr(value, "b"):
        try:
            return (float(value.r), float(value.g), float(value.b))
        except Exception:
            pass

    # Handle Blender Vector type by attribute presence
    if hasattr(value, "x") and hasattr(value, "y"):
        try:
            # Try to get up to 4D vector (x, y, z, w)
            components = [float(value.x), float(value.y)]
            if hasattr(value, "z"):
                components.append(float(value.z))
            if hasattr(value, "w"):
                components.append(float(value.w))
            return tuple(components)
        except Exception:
            pass

    # Convert any non-string, non-bytes iterable (e.g., Color, Vector, arrays) to tuple of floats
    if (
        hasattr(value, "__iter__")
        and hasattr(value, "__len__")
        and not isinstance(value, (str, bytes))
    ):
        try:
            return tuple(float(v) for v in value)
        except Exception:
            pass

    # Already a Python type (int, float, bool, str, bytes, etc.)
    if isinstance(value, (int, float, bool, str, bytes)):
        return value

    raise ValueError(
        f"Unsupported property type: {type(value)} for {value}. Please implement a conversion for this type."
    )


def to_python_identifier(name: str) -> str:
    """
    Converts a Blender property name to a Python identifier.
    """
    # Remove any special characters and replace spaces with underscores
    return name.replace(" ", "_").replace("-", "_").replace(".", "_").replace(",", "_")


def extract_properties_as_input_sockets(
    obj, node_obj, seen_names=None, seen_objs=None, prefix=None, depth=0, max_depth=20
):
    """
    Recursively extracts properties from a Blender RNA object and adds them as input sockets to the node.
    Properties from sub-objects are flattened into the node as ordinary inputs.
    Ensures enum-like values are always converted to strings.
    Also recurses into public attributes that are RNA sub-objects (e.g., color_ramp).
    Prevents infinite recursion by tracking visited objects by id or as_pointer.
    Prefixes input socket names with the sub-object name when recursing.
    """

    if prefix and prefix.endswith("rna_type"):
        return

    if seen_names is None:
        seen_names = set()
    if seen_objs is None:
        seen_objs = set()
    if depth > max_depth:
        return

    # Use as_pointer() if available, else id(obj)
    obj_key = None
    if hasattr(obj, "as_pointer"):
        try:
            obj_key = (obj.as_pointer(), type(obj))
        except Exception:
            obj_key = (id(obj), type(obj))
    else:
        obj_key = (id(obj), type(obj))
    if obj_key in seen_objs:
        return
    seen_objs.add(obj_key)

    bl_rna = getattr(obj, "bl_rna", None)
    if bl_rna is None:
        return

    # Extract all properties
    for prop_id, prop in bl_rna.properties.items():
        if should_ignore_property(prop_id, prop):
            continue
        base_name = to_python_identifier(prop_id)
        input_name = f"{prefix}_{base_name}" if prefix else base_name
        if input_name in seen_names:
            continue
        value = getattr(obj, prop_id, None)
        if hasattr(prop, "enum_items") and value is not None:
            py_value = str(value)
        elif isinstance(value, (str, bytes)):
            py_value = str(value)
        elif value is None:
            py_value = None
        else:
            py_value = to_python_datatype(value)
        input_socket_obj = InputSocket(
            name=input_name,
            node=node_obj,
            value=py_value,
            source=None,
        )
        node_obj.add_input_socket(input_socket_obj)
        seen_names.add(input_name)

    # Now recurse into sub-objects
    for prop_id, prop in bl_rna.properties.items():
        value = getattr(obj, prop_id, None)
        if hasattr(value, "bl_rna") and not isinstance(value, (str, bytes)):
            input_name = (
                f"{prefix}_{to_python_identifier(prop_id)}"
                if prefix
                else to_python_identifier(prop_id)
            )
            extract_properties_as_input_sockets(
                value,
                node_obj,
                seen_names,
                seen_objs,
                prefix=input_name,
                depth=depth + 1,
                max_depth=max_depth,
            )

    for attr in dir(obj):
        if attr.startswith("_"):
            continue
        if hasattr(bl_rna.properties, attr):
            continue
        try:
            value = getattr(obj, attr)
        except Exception:
            continue
        if hasattr(value, "bl_rna") and not isinstance(value, (str, bytes)):
            extract_properties_as_input_sockets(
                value,
                node_obj,
                seen_names,
                seen_objs,
                prefix=to_python_identifier(attr),
                depth=depth + 1,
                max_depth=max_depth,
            )


def create_node_from_blender_node(blender_node: bpy.types.Node) -> Node:
    """
    Converts a Blender node to a NodeSystem Node (without links).
    """
    node_type = blender_node.bl_idname.replace("ShaderNode", "")
    node_obj = Node(name=to_python_identifier(blender_node.name), node_type=node_type)

    extract_properties_as_input_sockets(blender_node, node_obj)

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

    add_node_input_sockets()
    add_output_sockets()
    deduplicate_input_socket_names(node_obj)

    # Treat color ramp as a synthetic input socket if present
    if not hasattr(blender_node, "color_ramp"):
        return node_obj

    ramp = blender_node.color_ramp
    if not hasattr(ramp, "elements"):
        return node_obj

    def color_to_tuple(color):
        # Convert Blender Color or similar to tuple of floats
        try:
            return tuple(float(c) for c in color)
        except Exception:
            return tuple()

    ramp_data = [
        {"position": float(e.position), "color": color_to_tuple(e.color)}
        for e in ramp.elements
    ]

    input_socket_obj = InputSocket(
        name="ColorRamp",
        node=node_obj,
        value=ramp_data,
        source=None,
    )
    node_obj.add_input_socket(input_socket_obj)

    return node_obj


def find_link_sockets(
    node_system: NodeSystem, blender_link, link_sockets_counters
) -> tuple[Optional[InputSocket], Optional[OutputSocket], list[str]]:
    """
    Given a node system and a blender link, find the corresponding input socket and source output socket.
    Handles deduplicated input sockets (e.g., Shader_1, Shader_2) for duplicate Blender socket names.
    Returns (input_socket, source_socket, all_candidate_names) or (None, None, all_candidate_names) if not found.
    The candidate names list is collected before any filtering, to aid debugging.
    Each candidate is formatted as 'node_name.socket_name'.
    """
    to_node_name = to_python_identifier(blender_link.to_node.name)
    to_socket_base = to_python_identifier(blender_link.to_socket.name)
    from_node_name = to_python_identifier(blender_link.from_node.name)
    from_socket_name = to_python_identifier(blender_link.from_socket.name)

    # Collect all input socket names from all nodes, with node name, before any filtering
    all_candidate_names = [
        f"{node.name}.{input_socket.name}"
        for node in node_system.nodes
        for input_socket in node.input_sockets
    ]

    for node in node_system.nodes:
        if node.name != to_node_name:
            continue
        matching_sockets = [
            s
            for s in node.input_sockets
            if s.name == to_socket_base
            or (
                s.name.startswith(f"{to_socket_base}_")
                and s.name[len(to_socket_base) + 1 :].isdigit()
            )
        ]

        def socket_sort_key(s):
            if s.name == to_socket_base:
                return 0
            try:
                return int(s.name[len(to_socket_base) + 1 :])
            except Exception:
                return 9999

        matching_sockets.sort(key=socket_sort_key)
        counter_key = (node.name, to_socket_base)
        idx = link_sockets_counters.get(counter_key, 0)
        if idx < len(matching_sockets):
            input_socket = matching_sockets[idx]
            link_sockets_counters[counter_key] = idx + 1
        else:
            input_socket = None
        source_node = next(
            (n for n in node_system.nodes if n.name == from_node_name), None
        )
        source_socket = None
        if source_node is not None:
            source_socket = next(
                (s for s in source_node.output_sockets if s.name == from_socket_name),
                None,
            )
        return input_socket, source_socket, all_candidate_names
    return None, None, all_candidate_names


def convert_from_blender(blender_nodes: bpy.types.NodeTree) -> NodeSystem:
    node_system = NodeSystem()
    link_sockets_counters: dict[tuple[str, str], int] = {}

    for blender_node in blender_nodes.nodes:
        node_obj = create_node_from_blender_node(blender_node)
        node_system.add_node(node_obj)

    # Set sources for input sockets
    for blender_link in blender_nodes.links:
        assert blender_link.to_socket is not None
        assert blender_link.to_node is not None
        assert blender_link.from_socket is not None
        assert blender_link.from_node is not None

        input_socket, source_socket, candidates = find_link_sockets(
            node_system, blender_link, link_sockets_counters
        )
        if input_socket is None or source_socket is None:
            print(
                f"[WARNING] Could not link: {blender_link.from_node.name}.{blender_link.from_socket.name} -> "
                f"{blender_link.to_node.name}.{blender_link.to_socket.name}\n"
                f"Candidates tried and rejected: {candidates}"
            )
            continue
        input_socket.source = source_socket

    return node_system
