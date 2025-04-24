import bpy
from .node_system import NodeSystem, Node, InputSocket, OutputSocket
from .common_properties import should_ignore_property

bl_info = {
    "name": "Node Code",
    "blender": (4, 4, 0),
    "category": "Node",
    "description": "Serialize node trees to text and back",
    "author": "Johan Walles",
    "version": (0, 0, 0),
    "location": "Shader Editor > View > Node Code...",
    "support": "FIXME",
    "doc_url": "FIXME",
}

# Updated convert_to_node_system to use should_ignore_property
def convert_to_node_system(node_tree):
    node_system = NodeSystem()

    for node in node_tree.nodes:
        # Create a Node object
        node_obj = Node(name=node.name, node_type=node.bl_idname)

        # Add input sockets for properties
        for prop_id, prop in node.bl_rna.properties.items():
            if should_ignore_property(prop_id, prop):
                continue

            socket_obj = InputSocket(
                name=prop_id,
                node=node_obj,
                value=getattr(node, prop_id, None),
                source=None
            )
            node_obj.add_input_socket(socket_obj)

        # Add input sockets for node inputs
        for input_socket in node.inputs:
            socket_obj = InputSocket(
                name=input_socket.name,
                node=node_obj,
                value=input_socket.default_value if hasattr(input_socket, 'default_value') else None,
                source=None  # Source will be set later if connected
            )
            node_obj.add_input_socket(socket_obj)

        # Add output sockets
        for output_socket in node.outputs:
            socket_obj = OutputSocket(
                name=output_socket.name,
                node=node_obj
            )
            node_obj.add_output_socket(socket_obj)

        # Add the node to the NodeSystem
        node_system.add_node(node_obj)

    # Set sources for input sockets
    for node in node_system.nodes:
        for input_socket in node.input_sockets:
            for link in node_tree.links:
                if link.to_socket.name == input_socket.name and link.to_node.name == node.name:
                    source_node = next(n for n in node_system.nodes if n.name == link.from_node.name)
                    source_socket = next(s for s in source_node.output_sockets if s.name == link.from_socket.name)
                    input_socket.source = source_socket

    return node_system

# Updated get_nodecode_script to accept a node_tree parameter
def get_nodecode_script(node_tree):
    node_system = convert_to_node_system(node_tree)

    node_system_str = str(node_system) if node_system else ""

    return "\n".join([
        "# Node Code Hello World Script",
        "print('Hello, World!')",
        node_system_str,
    ])

# Updated execute method to pass the current node tree
class NODECODE_OT_open_text_editor(bpy.types.Operator):
    bl_idname = "nodecode.open_text_editor"
    bl_label = "Open Node Code Script"
    bl_description = "Open a Python text editor with a Node Code script"

    def execute(self, context):
        # Get the current node tree
        node_tree = context.space_data.edit_tree if hasattr(context.space_data, 'edit_tree') else None

        # Create a new text block with a script based on the current node tree
        text_data = bpy.data.texts.new("Node_Code_Hello_World.py")
        text_data.write(get_nodecode_script(node_tree))

        # Open the text editor and display the new text block
        for area in context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                area.spaces.active.text = text_data
                break
        else:
            # If no text editor is open, switch an area to the text editor
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':  # Switch a 3D View area to a text editor
                    area.type = 'TEXT_EDITOR'
                    area.spaces.active.text = text_data
                    break

        return {'FINISHED'}

# Menu function to add the menu entry to the Shader Editor View menu
def nodecode_menu_func(self, context):
    self.layout.operator(NODECODE_OT_open_text_editor.bl_idname, text="Node Code...")

# Register and unregister functions
def register():
    bpy.utils.register_class(NODECODE_OT_open_text_editor)
    bpy.types.NODE_MT_view.append(nodecode_menu_func)

def unregister():
    bpy.utils.unregister_class(NODECODE_OT_open_text_editor)
    bpy.types.NODE_MT_view.remove(nodecode_menu_func)

if __name__ == "__main__":
    register()
