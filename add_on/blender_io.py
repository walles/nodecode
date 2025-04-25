import bpy
from .node_system import NodeSystem, Node, InputSocket, OutputSocket
from .common_properties import should_ignore_property


def convert_from_blender(node_tree: bpy.types.NodeTree) -> NodeSystem:
    node_system = NodeSystem()

    for blender_node in node_tree.nodes:
        # Create a Node object
        node_obj = Node(name=blender_node.name, node_type=blender_node.bl_idname)

        # Add input sockets for properties
        for prop_id, prop in blender_node.bl_rna.properties.items():
            if should_ignore_property(prop_id, prop):
                continue

            input_socket_obj = InputSocket(
                name=prop_id,
                node=node_obj,
                value=getattr(blender_node, prop_id, None),
                source=None,
            )
            node_obj.add_input_socket(input_socket_obj)

        # Add input sockets for node inputs
        for blender_input_socket in blender_node.inputs:
            input_socket_obj = InputSocket(
                name=blender_input_socket.name,
                node=node_obj,
                value=blender_input_socket.default_value
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
            for link in node_tree.links:
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
