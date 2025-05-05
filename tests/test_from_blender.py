from types import SimpleNamespace
import unittest

import example
from add_on.from_blender import convert_from_blender


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
