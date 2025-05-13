# Node Code

Copy / paste Blender node setups as text.

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
  `nodecode/` directory](nodecode/). Documented in a comment at the top of the
  file.
- `add_on`: Contains the Blender Node Code add-on.

# TODO

- Test roundtripping a node setup with a Color Ramp node
- Test node layout with Principled vs Diffuse and check the layout seems to get
  the node heights about right
- Regenerated the type stubs and check that the Mix Shader gets inputs named
  Shader_1 and Shader_2
- Make extract-blender-types.py extract Color Ramp nodes
- Make sure we handle node groups
  - Read them from Blender
  - Write them to Python
  - Read them from Python
  - Write them to Blender
- Make sure we handle reroute nodes
- Add an instructions comment to the generated code, and a link to the GitHub
  repository
- Verify no warnings are printed to the console on imports or exports
- Try export or import when the node area is the only open area
- When importing, make sure any problems are obviously reported to the user.
  Through in-code highlights or popups. Remove any assert statements from the
  import code.
- Document a versioning scheme based on the Blender version
- Add an example material to this README
- Don't name the exported editor "Node_Code_Hello_World.py", but rather
  something based on the material name
- Try removing all materials and exporting
- Try removing all objects and importing
- Publish Python type stubs to PyPI
- Publish the add-on to Blender Extensions
- Decorate some random tutorial(s) with Node Code
- Ensure the generated code has type hints where applicable
- Test that a generated nodecode file passes mypy without any complaints
- Adding multiple noise nodes in Blender names them Noise, Noise.001, Noise.002,
  etc. Convert this naming scheme to either just Noise (if there is only one),
  or to Noise_1, Noise_2, etc if there are multiple. This will look nicer in the
  Python code.
- Enable the add-on to show Node Code for a Geometry node setup
- Enable the add-on to show Node Code for a Compositing node setup
- Consider whether we could / should exclude default values in the generated
  code? This would make Principled BSDF nodes much easier to read.
- Resolve all FIXMEs
- Make sure the extracted-from-Blender Python stubs have no `Any` types

## Done

- Extract Python type stubs from Blender
- Make sure the Python stubs come with type hints
- Make a Blender add-on that can show Node Code for a Shaders node setup
  - This should be added to the View menu of the respective node editors. The
    menu entry should say "Node Code...".
  - Make sure the generated tree contains the Target dropdown for the Material
    Output node.
  - Make it generate Python code
  - Quote string values
  - Output tuple values as tuples
  - Make sure the generated code contains no forward references
  - Make main return the right value
- Implement converting Node Code to an internal node system object
- Right click the node area for Node Code access
- Enable the add-on to generate a node setup from Node Code source
- Try importing into a freshly started Blender instance
- Fix warnings when importing Principled BSDF nodes
- Test roundtripping the default material node setup
