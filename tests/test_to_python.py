import unittest
from add_on.to_python import render_value, render_float


class TestPythonIO(unittest.TestCase):
    def test_render_value_with_none(self) -> None:
        self.assertEqual(render_value(None), "None")

    def test_render_float(self) -> None:
        self.assertEqual(render_float(0.0), "0")
        self.assertEqual(render_float(0.00001234), "0.0000123")
        self.assertEqual(render_float(0.00012345), "0.000123")
        self.assertEqual(render_float(0.00123456), "0.00123")
        self.assertEqual(render_float(0.01234567), "0.0123")
        self.assertEqual(render_float(0.12345678), "0.123")
        self.assertEqual(render_float(1.23456789), "1.235")
        self.assertEqual(render_float(12.3456789), "12.35")
        self.assertEqual(render_float(123.456789), "123.5")
        self.assertEqual(render_float(1234.56789), "1234")
        self.assertEqual(render_float(12345.6789), "12345")
        self.assertEqual(render_float(123456.789), "123456")
        self.assertEqual(render_float(1234567.89), "1234567")

        self.assertEqual(render_float(-0.00001234), "-0.0000123")
        self.assertEqual(render_float(-12.3456789), "-12.35")
        self.assertEqual(render_float(-1234567.89), "-1234567")
