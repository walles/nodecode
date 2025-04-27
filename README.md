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
  - OK: Make sure the generated code contains no forward references
  - OK: Make main return the right value
- Enable the add-on to generate a node setup from Node Code source
- Test roundtripping the default material node setup
- Test roundtripping a node setup witha Color Ramp node
- Make extract-blender-types.py extract Color Ramp nodes
- Have a look at the Node Runner UI, https://github.com/Noah4ever/node_runner,
  about 1m45s into the video. Should we take inspiration from that? Right click
  the node area for Node Code access?
- Make sure we handle node groups
  - Read them from Blender
  - Write them to Python
  - Read them from Python
  - Write them to Blender
- Adding multiple noise nodes in Blender names them Noise, Noise.001, Noise.002,
  etc. Convert this naming scheme to either just Noise (if there is only one),
  or to Noise_1, Noise_2, etc if there are multiple. This will look nicer in the
  Python code.
- Enable the add-on to show Node Code for a Geometry node setup
- Enable the add-on to show Node Code for a Compositing node setup
- Consider whether we could / should exclude default values in the generated
  code? This would make Principled BSDF nodes much easier to read.
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
