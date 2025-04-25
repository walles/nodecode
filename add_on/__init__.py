import bpy

from .python_io import convert_to_python
from .blender_io import convert_from_blender

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


# Updated get_nodecode_script to accept a node_tree parameter
def get_nodecode_script(node_tree):
    node_system = convert_from_blender(node_tree)

    return convert_to_python(node_system)


# Updated execute method to pass the current node tree
class NODECODE_OT_open_text_editor(bpy.types.Operator):
    bl_idname = "nodecode.open_text_editor"
    bl_label = "Open Node Code Script"
    bl_description = "Open a Python text editor with a Node Code script"

    def execute(self, context):
        # Get the current node tree
        node_tree = (
            context.space_data.edit_tree
            if hasattr(context.space_data, "edit_tree")
            else None
        )

        # Create a new text block with a script based on the current node tree
        text_data = bpy.data.texts.new("Node_Code_Hello_World.py")
        text_data.write(get_nodecode_script(node_tree))

        # Open the text editor and display the new text block
        for area in context.screen.areas:
            if area.type == "TEXT_EDITOR":
                area.spaces.active.text = text_data
                break
        else:
            # If no text editor is open, switch an area to the text editor
            for area in context.screen.areas:
                if area.type == "VIEW_3D":  # Switch a 3D View area to a text editor
                    area.type = "TEXT_EDITOR"
                    area.spaces.active.text = text_data
                    break

        return {"FINISHED"}


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
