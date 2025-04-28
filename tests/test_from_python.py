import unittest
from add_on.from_python import convert_from_python
from add_on.node_system import NodeSystem, Node, InputSocket, OutputSocket


class TestFromPython(unittest.TestCase):
    def test_convert_from_python(self) -> None:
        nodecode_py = """
from nodecode.shading import *

def main() -> OutputMaterial:
    Diffuse_BSDF = BsdfDiffuse(
        Color=(0.800, 0.800, 0.800, 1.000),
        Roughness=0,
        Normal=(0, 0, 0),
        Weight=0)

    Material_Output = OutputMaterial(
        is_active_output=True,
        target="ALL",
        Surface=Diffuse_BSDF.BSDF(),
        Volume=None,
        Displacement=(0, 0, 0),
        Thickness=0)

    return Material_Output
        """

        diffuse_node = Node("Diffuse_BSDF", "BsdfDiffuse")
        diffuse_node.add_input_socket(
            InputSocket("Color", diffuse_node, (0.800, 0.800, 0.800, 1.000), None)
        )
        diffuse_node.add_input_socket(InputSocket("Roughness", diffuse_node, 0, None))
        diffuse_node.add_input_socket(
            InputSocket("Normal", diffuse_node, (0, 0, 0), None)
        )
        diffuse_node.add_input_socket(InputSocket("Weight", diffuse_node, 0, None))

        diffuse_bsdf_output = OutputSocket("BSDF", diffuse_node)
        diffuse_node.add_output_socket(diffuse_bsdf_output)

        output_node = Node("Material_Output", "OutputMaterial")
        output_node.add_input_socket(
            InputSocket("is_active_output", output_node, True, None)
        )
        output_node.add_input_socket(InputSocket("target", output_node, "ALL", None))
        output_node.add_input_socket(
            InputSocket("Surface", output_node, None, diffuse_bsdf_output)
        )
        output_node.add_input_socket(InputSocket("Volume", output_node, None, None))
        output_node.add_input_socket(
            InputSocket("Displacement", output_node, (0, 0, 0), None)
        )
        output_node.add_input_socket(InputSocket("Thickness", output_node, 0, None))

        node_system = NodeSystem()
        node_system.add_node(diffuse_node)
        node_system.add_node(output_node)

        self.maxDiff = None
        self.assertMultiLineEqual(
            str(convert_from_python(nodecode_py)), str(node_system)
        )
