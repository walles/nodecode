import unittest
from add_on.from_python import convert_from_python

import example


class TestFromPython(unittest.TestCase):
    def test_convert_from_python(self) -> None:
        nodecode_py = """
from nodecode.shading import *

def main() -> OutputMaterial:
    Diffuse_BSDF = BsdfDiffuse(
        Color=(0.800, 0.800, 0.800, 1.000),
        Roughness=0.0,
        Normal=(0.0, 0.0, 0.0),
        Weight=0.0)

    Material_Output = OutputMaterial(
        is_active_output=True,
        target="ALL",
        Surface=Diffuse_BSDF.BSDF(),
        Volume=None,
        Displacement=(0.0, 0.0, 0.0),
        Thickness=0.0)

    return Material_Output
        """

        self.maxDiff = None
        self.assertMultiLineEqual(
            str(convert_from_python(nodecode_py)), str(example.diffuse_material())
        )
