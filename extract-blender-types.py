# Extract Node Code types from a running Blender instance.
#
# Instructions:
# 1. Open Blender
# 2. Save the default scene as Untitled.blend in the same directory as this script
# 3. Open the Scripting workspace
# 4. Click the "New" button to create a new script
# 5. Copy and paste this code into the script editor
# 6. Run the script by clicking the "Run Script" button
#
# `git diff` should now show the changes to the stub files in the `nodecode` folder.

import bpy
import os
import re
from collections import defaultdict
from datetime import datetime

# Output folder relative to the blend file
base_path = bpy.path.abspath("//nodecode")
os.makedirs(base_path, exist_ok=True)

# Common to all node types, storing these is not relevant for getting the right
# output.
COMMON_NODE_PROPERTIES = {
    'bl_description',
    'bl_height_default',
    'bl_height_max',
    'bl_height_min',
    'bl_icon',
    'bl_idname',
    'bl_label',
    'bl_width_default',
    'bl_width_max',
    'bl_width_min',
    'color',
    'height',
    'hide',
    'label',
    'location_absolute',
    'location',
    'mute',
    'name',
    'parent',
    'select',
    'show_options',
    'show_preview',
    'show_texture',
    'use_custom_color',
    'warning_propagation',
    'width',
}

def python_type(bl_type):
    return {
        'VALUE': 'float',
        'INT': 'int',
        'BOOLEAN': 'bool',
        'RGBA': 'Tuple[float, float, float, float]',
        'VECTOR': 'Tuple[float, float, float]',
        'STRING': 'str',
        'SHADER': 'Any',
        'OBJECT': 'Any',
        'GEOMETRY': 'Any',
        'IMAGE': 'Any',
        'COLLECTION': 'Any',
    }.get(bl_type, 'Any')

def pprint(obj) -> str:
    """Pretty print a Blender object."""
    if hasattr(obj, 'bl_rna'):
        return f"{obj.bl_rna.identifier}({', '.join(f'{k}={v}' for k, v in obj.items())})"
    return str(obj)

def sanitize_name(name):
    sanitized = re.sub(r'\W|^(?=\d)', '_', name)
    if sanitized == "False":
        sanitized = "on_False"
    elif sanitized == "True":
        sanitized = "on_True"

    if not sanitized:
        raise ValueError(f"Cannot sanitize name: {name}")

    return sanitized

def escape_doc(s: str) -> str:
    escaped = s
    escaped = escaped.replace("\n", "\n\n")
    return escaped.strip()

def write_stub_file(domain, node_prefix, tree_type):
    filename = os.path.join(base_path, f"{domain}.pyi")
    with open(filename, "w", encoding="utf-8") as f:
        # Get Blender version and current time
        blender_version = bpy.app.version_string
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write the comment at the top of the file
        f.write(f"# Generated from Blender {blender_version} on {current_time}\n")
        f.write("from typing import Any, Tuple\n\n")

        if tree_type == "ShaderNodeTree":
            mat = bpy.data.materials.new("TempMat")
            mat.use_nodes = True
            tree = mat.node_tree
        elif tree_type == "CompositorNodeTree":
            bpy.context.scene.use_nodes = True
            tree = bpy.context.scene.node_tree
        elif tree_type == "GeometryNodeTree":
            tree = bpy.data.node_groups.new(name="TempGeoTree", type="GeometryNodeTree")
        else:
            print(f"Unknown tree type: {tree_type}")
            return

        node_classes = [cls for cls in dir(bpy.types) if cls.startswith(node_prefix)]

        for cls_name in sorted(node_classes):
            node_type = getattr(bpy.types, cls_name)
            node_idname = node_type.bl_rna.identifier

            try:
                assert tree is not None
                node = tree.nodes.new(type=node_idname)
            except:
                continue

            if node is None:
                continue

            short_name = cls_name[len(node_prefix):]
            bl_label = getattr(node, 'bl_label', short_name)
            bl_description = getattr(node, 'bl_description', '')
            class_doc = escape_doc(bl_description or bl_label)
            f.write(f"class {short_name}:\n")
            f.write(f'    """{class_doc}"""\n')

            # --- NODE PROPERTIES WITH UI ELEMENTS ---
            ui_properties = []
            for prop_id, prop in node.bl_rna.properties.items():
                # Skip properties that are hidden or read-only
                if prop.is_hidden or prop.is_readonly:
                    continue

                # Skip properties that are common to all nodes
                if prop_id in COMMON_NODE_PROPERTIES:
                    continue

                prop_type = python_type(prop.type)
                ui_properties.append(f"{sanitize_name(prop_id)}: {prop_type}")

            # --- INPUTS ---
            input_counts = defaultdict(int)
            for s in node.inputs:
                input_counts[s.name] += 1

            input_name_indices = defaultdict(int)
            input_args = []
            for s in node.inputs:
                if not s.name:
                    print(f"Warning: Input {pprint(s)} has no name, skipping...")
                    continue

                count = input_counts[s.name]
                base = sanitize_name(s.name)
                if count == 1:
                    name = base
                else:
                    input_name_indices[base] += 1
                    name = f"{base}{input_name_indices[base]}"
                hint = python_type(s.type)
                input_args.append(f"{name}: {hint} = ...")

            # Combine UI properties and inputs
            all_args = ui_properties + input_args
            f.write(f"    def __init__(self, {', '.join(all_args)}) -> None: ...\n")

            # --- OUTPUTS ---
            output_counts = defaultdict(int)
            for s in node.outputs:
                output_counts[s.name] += 1

            output_indices = defaultdict(int)
            for s in node.outputs:
                if not s.name:
                    print(f"Warning: Output {pprint(s)} has no name, skipping...")
                    continue

                count = output_counts[s.name]
                base = sanitize_name(s.name)
                if count == 1:
                    name = base
                else:
                    output_indices[base] += 1
                    name = f"{base}{output_indices[base]}"
                return_type = python_type(s.type)
                description = escape_doc(getattr(s, 'description', '') or s.name)
                f.write(f'    def {name}(self) -> {return_type}: """{description}"""\n')

            f.write("\n")
            tree.nodes.remove(node)

        if tree_type == "ShaderNodeTree":
            bpy.data.materials.remove(mat, do_unlink=True)
        elif tree_type == "GeometryNodeTree":
            bpy.data.node_groups.remove(tree, do_unlink=True)

    print(f"✅ Generated {filename}")

# Generate .pyi stubs
write_stub_file("shading", "ShaderNode", "ShaderNodeTree")
write_stub_file("geometry", "GeometryNode", "GeometryNodeTree")
write_stub_file("compositing", "CompositorNode", "CompositorNodeTree")

# Ensure package file exists
init_path = os.path.join(base_path, "__init__.py")
with open(init_path, "w") as init_file:
    init_file.write("# nodecode package stub\n")

print(f"📦 .pyi stub files with docstrings saved in: {base_path}")
