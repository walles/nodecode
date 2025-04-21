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

# Output folder: relative to the .blend file
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

def quote_name(name):
    return name if name.isidentifier() else f'"{name}"'

def sanitize_method_name(name):
    # Ensure the name is a valid Python identifier
    name = re.sub(r'\W|^(?=\d)', '_', name)
    return name

def write_stub_file(domain, node_prefix, tree_type):
    filename = os.path.join(base_path, f"{domain}.py")
    with open(filename, "w") as f:
        f.write("from typing import Any, Tuple\n\n")

        # Create a temporary node tree
        if tree_type == "ShaderNodeTree":
            mat = bpy.data.materials.new("TempMat")
            mat.use_nodes = True
            tree = mat.node_tree
        elif tree_type == "CompositorNodeTree":
            scene = bpy.context.scene
            scene.use_nodes = True
            tree = scene.node_tree
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
                continue  # Skip nodes that can't be instantiated

            if node is None:
                continue

            inputs = []
            for input_socket in node.inputs:
                name = input_socket.name
                hint = python_type(input_socket.type)
                inputs.append(f"{quote_name(name)}: {hint} = ...")

            short_name = cls_name[len(node_prefix):]
            f.write(f"class {short_name}:\n")
            if inputs:
                f.write(f"    def __init__(self, {', '.join(inputs)}) -> None: ...\n")
            else:
                f.write("    def __init__(self) -> None: ...\n")

            for output_socket in node.outputs:
                method_name = sanitize_method_name(output_socket.name)
                return_type = python_type(output_socket.type)
                f.write(f"    def {method_name}(self) -> {return_type}: ...\n")

            f.write("\n")

            if node is not None:
                tree.nodes.remove(node)

        # Clean up
        if tree_type == "ShaderNodeTree":
            bpy.data.materials.remove(mat, do_unlink=True)
        elif tree_type == "GeometryNodeTree":
            bpy.data.node_groups.remove(tree, do_unlink=True)

    print(f"✅ Generated {filename}")

# Write all domains
write_stub_file("shading", "ShaderNode", "ShaderNodeTree")
write_stub_file("geometry", "GeometryNode", "GeometryNodeTree")
write_stub_file("compositing", "CompositorNode", "CompositorNodeTree")

# Create __init__.py to make nodecode a package
init_path = os.path.join(base_path, "__init__.py")
with open(init_path, "w") as init_file:
    init_file.write("# nodecode package\n")

print(f"📦 nodecode stubs written to: {base_path}")
