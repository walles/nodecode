import bpy
from bpy.types import Operator
from bpy.props import StringProperty

from .to_python import convert_to_python
from .blender_io import convert_from_blender


# Updated get_nodecode_script to accept a node_tree parameter
def get_nodecode_script(node_tree) -> str:
    node_system = convert_from_blender(node_tree)

    return convert_to_python(node_system)


# Updated execute method to pass the current node tree
class NODECODE_OT_export_node_code(bpy.types.Operator):
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

        # Without this the editor will show the end of the text, and sometimes
        # not even that.
        text_data.cursor_set(line=0, character=0)

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


# Dialog operator for importing Node Code
class NODECODE_OT_import_node_code(Operator):
    bl_idname = "nodecode.import_node_code"
    bl_label = "Import Node Code"
    bl_description = "Open a dialog to paste Node Code for import"

    # Blender needs a : annotation, which clashes with mypy's idea about how to
    # do type checking. Tell mypy to ignore this line.
    node_code: StringProperty(  # type: ignore[valid-type]
        name="Node Code", description="Paste your Node Code here", default=""
    )

    def execute(self, context):
        self.report({"INFO"}, f"Node Code: {self.node_code}")
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "node_code", text="Paste Node Code")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


def nodecode_menu_func(self, context):
    self.layout.separator()  # Add a divider
    self.layout.operator(
        NODECODE_OT_export_node_code.bl_idname, text="Export Node Code..."
    )
    self.layout.operator_context = "INVOKE_DEFAULT"
    self.layout.operator(
        NODECODE_OT_import_node_code.bl_idname, text="Import Node Code..."
    )


# Register and unregister functions
def register():
    bpy.utils.register_class(NODECODE_OT_export_node_code)
    bpy.utils.register_class(NODECODE_OT_import_node_code)
    bpy.types.NODE_MT_context_menu.append(nodecode_menu_func)  # Add to right-click menu


def unregister():
    bpy.utils.unregister_class(NODECODE_OT_export_node_code)
    bpy.utils.unregister_class(NODECODE_OT_import_node_code)
    bpy.types.NODE_MT_context_menu.remove(
        nodecode_menu_func
    )  # Remove from right-click menu
