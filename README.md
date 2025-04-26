# Node Code

Enable copy / pasting Blender node setups as text.

Imagine for example that you're looking at a tutorial to make a procedural wood
shader.

Without Node Code, to get the completed material you would have to either:

1. Draw the node setup by hand in Blender, based on the tutorial
2. If the tutorial comes with a `.blend` file, download that and append the
   material to your own file.

With Node Code, the tutorial can just include a text with the node setup.

You copy the text, paste it in Blender, and voilà! You have the node setup ready to
go.

The text format is a subset of Python, so you can open Node Code files in a text
editor, and edit them there.

# Hacking

Run `tox` frequently to verify your changes.

## Layout

- `extract-blender-types.py`: Extracts Python type stubs from Blender into [the
  `nodecode/` directory](nodecode/). Documented in [the `nodecode/`
  README.md](nodecode/README.md)
- `add_on`: Contains the Blender Node Code add-on.

# TODO

- Make a Blender add-on that can show Node Code for a Shaders node setup
  - OK: This should be added to the View menu of the respective node editors.
    The menu entry should say "Node Code...".
  - OK: Make sure the generated tree contains the Target dropdown for the
    Material Output node.
  - OK: Make it generate Python code
  - OK: Quote string values
  - OK: Output tuple values as tuples
  - Make main return the right value
  - Make sure the generated code contains no forward references
  - After reading a blender node setup, call a normalize function to deduplicate
    node names by adding numbered suffixes when needed
- Enable the add-on to show Node Code for a Geometry node setup
- Enable the add-on to show Node Code for a Compositing node setup
- Enable the add-on to create a new node setup (or overwrite an existing one?)
  from a Node Code file
- Document a versioning scheme based on the Blender version
- Resolve all FIXMEs
- Publish Python type stubs to PyPI
- Publish the add-on to Blender Extensions
- Ensure the generated code has type hints where applicable
- Test that a generated nodecode file passes mypy without any complaints
- Make sure the extracted-from-Blender Python stubs have no `Any` types

## Done

- Extract Python type stubs from Blender
- Make sure the Python stubs come with type hints
