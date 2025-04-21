# NodeCode

Enable copy / pasting Blender node setups as text.

Imagine for example that you're looking at a tutorial to make a procedural wood
shader.

Without NodeCode, to get the completed material you would have to either:
1. Draw the node setup by hand in Blender, based on the tutorial
2. If the tutorial comes with a `.blend` file, download that and append the
   material to your own file.

With NodeCode, the tutorial can just include a text with the node setup.

You copy the text, paste it in Blender, and voilà! You have the node setup ready to
go.

The text format is a subset of Python, so you can open NodeCode files in a text
editor, and edit them there.

# TODO
- Make a Blender add-on that can show NodeCode for any node setup
  - Shaders
  - Geometry
  - Compositing
  - This should be added to the View menu of the respective node editors. The
    menu entry should say "NodeCode...".
- Enable the add-on to create a new node setup (or overwrite an existing one?)
  from a NodeCode file
- Document a versioning scheme based on the Blender version
- Publish Python type stubs to PyPI
- Publish the add-on to Blender Extensions
- Ensure the generated code has type hints where applicable
- Test that a generated nodecode file passes mypy without any complaints
- Make sure the extracted-from-Blender Python stubs have no `Any` types

## Done
- Extract Python type stubs from Blender
- Make sure the Python stubs come with type hints
