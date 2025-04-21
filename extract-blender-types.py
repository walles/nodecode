# Extract NodeCode types from a running Blender instance.
#
# Instructions:
# 1. Open Blender
# 2. Open the Scripting workspace
# 3. Click the "New" button to create a new script
# 4. Copy and paste this code into the script editor
# 5. Run the script by clicking the "Run Script" button
# 6. The generated files will be saved in a folder named "nodecode" next to your .blend file

import bpy
import os
import re
from collections import defaultdict

# Output folder relative to the blend file
base_path = bpy.path.abspath("//nodecode")
os.makedirs(base_path, exist_ok=True)

def python_type(bl_type):
    return {
        'VALUE': 'float',
        'INT': 'int',
        'BOOLEAN': 'bool',
        'RGBA': 'tuple[float, float, float, float]',
        'VECTOR': 'tuple[float, float, float]',
        'STRING': 'str',
        'SHADER': 'Any',
        'OBJECT': 'Any',
        'GEOMETRY': 'Any',
        'IMAGE': 'Any',
        'COLLECTION': 'Any',
    }.get(bl_type, 'Any')

def sanitize_name(name):
    return re.sub(r'\W|^(?=\d)', '_', name)

def escape_doc(s: str) -> str:
    return s.replace('"""', '\"\"\"').strip()

def write_stub_file(domain, node_prefix, tree_type):
    filename = os.path.join(base_path, f"{domain}.pyi")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("from typing import Any, Tuple\n\n")

        # Create a temporary node tree
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
                node = tree.nodes.new(type=node_idname)
            except:
                continue  # Skip nodes that can’t be instantiated

            if node is None:
                continue

            # Count input socket names
            input_counts = defaultdict(int)
            for s in node.inputs:
                input_counts[s.name] += 1

            inputs = []
            input_name_indices = defaultdict(int)
            for s in node.inputs:
                count = input_counts[s.name]
                base = sanitize_name(s.name)
                if count == 1:
                    name = base
                else:
                    input_name_indices[base] += 1
                    name = f"{base}{input_name_indices[base]}"
                hint = python_type(s.type)
                inputs.append(f"{name}: {hint} = ...")

            short_name = cls_name[len(node_prefix):]
            bl_label = getattr(node, 'bl_label', short_name)
            bl_description = getattr(node, 'bl_description', '')
            class_doc = escape_doc(bl_description or bl_label)

            f.write(f"class {short_name}:\n")
            f.write(f'    """{class_doc}"""\n')

            # Write __init__ signature
            if inputs:
                f.write(f"    def __init__(self, {', '.join(inputs)}) -> None: ...\n")
            else:
                f.write("    def __init__(self) -> None: ...\n")

            # Handle output sockets
            output_counts = defaultdict(int)
            for s in node.outputs:
                output_counts[s.name] += 1

            output_indices = defaultdict(int)
            for s in node.outputs:
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

            # Clean up
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
