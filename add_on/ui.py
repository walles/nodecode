import bpy
from bpy.types import Operator, SpaceTextEditor, Screen
import textwrap

from .to_python import convert_to_python
from .from_python import convert_from_python
from .from_blender import convert_from_blender
from .to_blender import create_blender_material


# Updated get_nodecode_script to accept a node_tree parameter
def get_nodecode_script(node_tree) -> str:
    node_system = convert_from_blender(node_tree)

    return convert_to_python(node_system)


def get_text_editor(screen: Screen) -> SpaceTextEditor:
    for area in screen.areas:
        if area.type == "TEXT_EDITOR":
            assert isinstance(area.spaces.active, SpaceTextEditor), (
                "Expected SpaceTextEditor"
            )
            return area.spaces.active

    # No text editor is open, switch an area to the text editor
    for area in screen.areas:
        if area.type == "VIEW_3D":  # Switch a 3D View area to a text editor
            area.type = "TEXT_EDITOR"
            assert isinstance(area.spaces.active, SpaceTextEditor), (
                "Expected SpaceTextEditor"
            )
            return area.spaces.active

    raise RuntimeError("Unable to find or create a text editor area.")


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
        text = bpy.data.texts.new("Node_Code_Hello_World.py")
        text.write(get_nodecode_script(node_tree))

        # Without this the editor will show the end of the text, and sometimes
        # not even that.
        text.cursor_set(line=0, character=0)

        get_text_editor(context.screen).text = text

        return {"FINISHED"}


# Dialog operator for importing Node Code
class NODECODE_OT_material_import_node_code(Operator):
    bl_idname = "nodecode.import_node_code"
    bl_label = "Import Node Code"
    bl_description = "Open a text editor where Node Code can be pasted for import"

    def execute(self, context):
        text = bpy.data.texts.new("Node_Code_Import.py")
        text.write(
            textwrap.dedent("""
        # Right-click and choose "Import Node Code" to import the code after pasting it here.
        """).lstrip()
        )

        # Without this the editor will show the end of the text, and sometimes
        # not even that.
        text.cursor_set(line=0, character=0)

        get_text_editor(context.screen).text = text

        return {"FINISHED"}


class NODECODE_OT_text_editor_import_node_code(Operator):
    bl_idname = "nodecode.text_editor_import_node_code"
    bl_label = "Import Node Code"
    bl_description = "Import Node Code from the text editor"

    def execute(self, context):
        # Get the active text editor
        text_editor = get_text_editor(context.screen)

        # Get the text block
        text_block = text_editor.text
        assert text_block is not None, "No text block found in the text editor"

        # Convert the text block content into a NodeSystem
        node_system = convert_from_python(text_block.as_string())

        # Convert the NodeSystem into a new Blender material
        material = create_blender_material(node_system)

        # Set the new material as the active material for the active object.
        # This also makes the Shader Editor switch to the new material.
        if context.object:
            context.object.active_material = material

        return {"FINISHED"}


def nodecode_material_menu_func(self, context):
    self.layout.separator()  # Add a divider
    self.layout.operator(
        NODECODE_OT_export_node_code.bl_idname, text="Export Node Code..."
    )
    self.layout.operator_context = "INVOKE_DEFAULT"
    self.layout.operator(
        NODECODE_OT_material_import_node_code.bl_idname, text="Import Node Code..."
    )


def nodecode_text_editor_menu_func(self, context):
    self.layout.separator()  # Add a divider
    self.layout.operator_context = "INVOKE_DEFAULT"
    self.layout.operator(
        NODECODE_OT_text_editor_import_node_code.bl_idname, text="Import Node Code"
    )


# Maintain a list of registered classes to avoid duplicate registration
classes = [
    NODECODE_OT_export_node_code,
    NODECODE_OT_material_import_node_code,
    NODECODE_OT_text_editor_import_node_code,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.NODE_MT_context_menu.append(nodecode_material_menu_func)
    bpy.types.TEXT_MT_context_menu.append(nodecode_text_editor_menu_func)


def unregister():
    for cls in reversed(classes):  # Unregister in reverse order of registration
        bpy.utils.unregister_class(cls)

    bpy.types.NODE_MT_context_menu.remove(nodecode_material_menu_func)
    bpy.types.TEXT_MT_context_menu.remove(nodecode_text_editor_menu_func)
