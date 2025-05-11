import unittest
from types import SimpleNamespace
from add_on.to_blender import apply_input_socket_to_blender_node
from add_on.node_system import InputSocket, Node


class TestApplyInputSocketToBlenderNode(unittest.TestCase):
    def test_set_input_socket_value(self):
        # Mock Blender node with an input socket
        mock_input = SimpleNamespace(name="TestInput", default_value=None)
        mock_node = SimpleNamespace(
            inputs={"TestInput": mock_input},
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
            inputs = {}
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
            inputs = {}

        mock_node = MockNode()
        dummy_node = Node("Dummy", "DummyType")
        input_socket = InputSocket(
            name="not_found", node=dummy_node, value=1, source=None
        )
        # Should not raise, just print a warning
        apply_input_socket_to_blender_node(mock_node, input_socket)  # type: ignore


if __name__ == "__main__":
    unittest.main()
