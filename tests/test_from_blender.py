from types import SimpleNamespace
import unittest

import example
from add_on.from_blender import (
    convert_from_blender,
    create_node_from_blender_node,
    find_link_sockets,
)
from add_on.node_system import Node, NodeSystem, InputSocket, OutputSocket


class TestConvertFromBlender(unittest.TestCase):
    def test_convert_from_blender(self) -> None:
        diffuse_bsdf = SimpleNamespace(
            name="Diffuse BSDF",
            type="ShaderNodeBsdfDiffuse",
            bl_idname="ShaderNodeBsdfDiffuse",
            bl_rna=SimpleNamespace(properties=SimpleNamespace(items=lambda: [])),
            inputs=[
                SimpleNamespace(
                    name="Color",
                    default_value=(0.8, 0.8, 0.8, 1.0),
                ),
                SimpleNamespace(
                    name="Roughness",
                    default_value=0.0,
                ),
                SimpleNamespace(
                    name="Normal",
                    default_value=(0.0, 0.0, 0.0),
                ),
                SimpleNamespace(
                    name="Weight",
                    default_value=0.0,
                ),
            ],
            outputs=[
                SimpleNamespace(
                    name="BSDF",
                ),
            ],
        )

        material_output = SimpleNamespace(
            name="Material Output",
            type="ShaderNodeOutputMaterial",
            bl_idname="ShaderNodeOutputMaterial",
            bl_rna=SimpleNamespace(properties=SimpleNamespace(items=lambda: [])),
            inputs=[
                SimpleNamespace(
                    name="is_active_output",
                    default_value=True,
                ),
                SimpleNamespace(
                    name="target",
                    default_value="ALL",
                ),
                SimpleNamespace(
                    name="Surface",
                    default_value=None,
                ),
                SimpleNamespace(
                    name="Volume",
                    default_value=None,
                ),
                SimpleNamespace(
                    name="Displacement",
                    default_value=(0.0, 0.0, 0.0),
                ),
                SimpleNamespace(
                    name="Thickness",
                    default_value=0.0,
                ),
            ],
            outputs=[],
        )

        class MockNodeTree:
            def __init__(self):
                self.nodes = [
                    diffuse_bsdf,
                    material_output,
                ]
                self.links = [
                    SimpleNamespace(
                        from_node=diffuse_bsdf,
                        from_socket=SimpleNamespace(name="BSDF"),
                        to_node=material_output,
                        to_socket=SimpleNamespace(name="Surface"),
                    )
                ]

        node_tree = MockNodeTree()
        actual = convert_from_blender(node_tree)  # type: ignore
        expected = example.diffuse_material()

        self.maxDiff = None
        self.assertMultiLineEqual(str(actual), str(expected))


class TestCreateNodeFromBlenderNode(unittest.TestCase):
    def test_basic_node(self):
        # Minimal mock Blender node using SimpleNamespace for clarity
        mock_blender_node = SimpleNamespace(
            name="Test Node",
            bl_idname="ShaderNodeTest",
            bl_rna=SimpleNamespace(properties=SimpleNamespace(items=lambda: [])),
            inputs=[SimpleNamespace(name="InputA", default_value=1.0)],
            outputs=[SimpleNamespace(name="OutputA")],
        )
        # Patch items() to return empty list for properties
        mock_blender_node.bl_rna.properties.items = lambda: []

        node = create_node_from_blender_node(mock_blender_node)  # type: ignore
        self.assertIsInstance(node, Node)
        self.assertEqual(node.name, "Test_Node")
        self.assertEqual(node.node_type, "Test")
        self.assertEqual(len(node.input_sockets), 1)
        self.assertEqual(node.input_sockets[0].name, "InputA")
        self.assertEqual(node.input_sockets[0].value, 1.0)
        self.assertEqual(len(node.output_sockets), 1)
        self.assertEqual(node.output_sockets[0].name, "OutputA")

    def test_mix_shader_duplicate_input_names(self):
        # Mock Blender Mix Shader node with two 'Shader' inputs
        mock_blender_node = SimpleNamespace(
            name="Mix Shader",
            bl_idname="ShaderNodeMixShader",
            bl_rna=SimpleNamespace(properties=SimpleNamespace(items=lambda: [])),
            inputs=[
                SimpleNamespace(name="Fac", default_value=0.5),
                SimpleNamespace(name="Shader", default_value=None),
                SimpleNamespace(name="Shader", default_value=None),
            ],
            outputs=[SimpleNamespace(name="Shader")],
        )
        mock_blender_node.bl_rna.properties.items = lambda: []

        node = create_node_from_blender_node(mock_blender_node)  # type: ignore
        self.assertIsInstance(node, Node)
        self.assertEqual(node.name, "Mix_Shader")
        self.assertEqual(node.node_type, "MixShader")
        self.assertEqual(len(node.input_sockets), 3)
        self.assertEqual(node.input_sockets[0].name, "Fac")
        self.assertEqual(node.input_sockets[1].name, "Shader_1")
        self.assertEqual(node.input_sockets[2].name, "Shader_2")
        self.assertEqual(len(node.output_sockets), 1)
        self.assertEqual(node.output_sockets[0].name, "Shader")


class TestFindLinkSockets(unittest.TestCase):
    def test_find_link_sockets_happy_case(self):
        # Create two nodes: source and target
        source_node = Node(name="Source_Node", node_type="TestType")
        target_node = Node(name="Target_Node", node_type="TestType")

        # Add output socket to source node
        source_output = OutputSocket(name="Out", node=source_node)
        source_node.add_output_socket(source_output)

        # Add input socket to target node
        target_input = InputSocket(name="In", node=target_node, value=None, source=None)
        target_node.add_input_socket(target_input)

        # Create node system
        node_system = NodeSystem()
        node_system.add_node(source_node)
        node_system.add_node(target_node)

        # Mock a blender_link with matching names
        blender_link = SimpleNamespace(
            from_node=SimpleNamespace(name="Source Node"),
            from_socket=SimpleNamespace(name="Out"),
            to_node=SimpleNamespace(name="Target Node"),
            to_socket=SimpleNamespace(name="In"),
        )

        # Should resolve to the correct sockets
        input_socket, output_socket = find_link_sockets(node_system, blender_link)
        self.assertIs(input_socket, target_input)
        self.assertIs(output_socket, source_output)
