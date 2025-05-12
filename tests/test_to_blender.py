import unittest
from types import SimpleNamespace
from add_on.to_blender import apply_input_socket_to_blender_node
from add_on.node_system import InputSocket, Node


class TestApplyInputSocketToBlenderNode(unittest.TestCase):
    def test_set_input_socket_value(self):
        # Mock Blender node with an input socket
        mock_input = SimpleNamespace(name="TestInput", default_value=None)
        mock_node = SimpleNamespace(
            inputs=[mock_input],  # Changed from dict to list
            bl_idname="ShaderNodeTest",
        )
        dummy_node = Node("Dummy", "DummyType")
        input_socket = InputSocket(
            name="TestInput", node=dummy_node, value=42, source=None
        )
        apply_input_socket_to_blender_node(mock_node, input_socket)  # type: ignore
        self.assertEqual(mock_input.default_value, 42)

    def test_set_node_property(self):
        # Mock Blender node with a property, but no input socket
        class MockNode:
            bl_idname = "ShaderNodeTest"
            inputs = []  # Changed from dict to list
            test_property = 0

        mock_node = MockNode()
        dummy_node = Node("Dummy", "DummyType")
        input_socket = InputSocket(
            name="test_property", node=dummy_node, value=123, source=None
        )
        apply_input_socket_to_blender_node(mock_node, input_socket)  # type: ignore
        self.assertEqual(mock_node.test_property, 123)

    def test_warn_on_missing(self):
        # Mock Blender node with neither input socket nor property
        class MockNode:
            bl_idname = "ShaderNodeTest"
            inputs = []  # Changed from dict to list

        mock_node = MockNode()
        dummy_node = Node("Dummy", "DummyType")
        input_socket = InputSocket(
            name="not_found", node=dummy_node, value=1, source=None
        )
        # Should not raise, just print a warning
        apply_input_socket_to_blender_node(mock_node, input_socket)  # type: ignore

    def test_set_duplicate_input_socket_values(self):
        # Mock Blender node with two inputs of the same base name, using Blender's naming convention
        blender_input_1 = SimpleNamespace(name="Shader", default_value=None)
        blender_input_2 = SimpleNamespace(name="Shader_001", default_value=None)
        # Simulate Blender's node.inputs as a list
        blender_node = SimpleNamespace(
            inputs=[blender_input_1, blender_input_2],  # Changed from dict to list
            bl_idname="ShaderNodeMixShader",
        )
        dummy_node = Node("Dummy", "DummyType")
        input_socket_1 = InputSocket(
            name="Shader_1", node=dummy_node, value="A", source=None
        )
        input_socket_2 = InputSocket(
            name="Shader_2", node=dummy_node, value="B", source=None
        )
        # Call the actual function under test
        apply_input_socket_to_blender_node(blender_node, input_socket_1)  # type: ignore
        apply_input_socket_to_blender_node(blender_node, input_socket_2)  # type: ignore
        self.assertEqual(blender_input_1.default_value, "A")
        self.assertEqual(blender_input_2.default_value, "B")


if __name__ == "__main__":
    unittest.main()
