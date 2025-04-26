import unittest
from add_on.python_io import render_value


class TestRenderValue(unittest.TestCase):
    def test_render_value_with_none(self):
        self.assertEqual(render_value(None), "None")


if __name__ == "__main__":
    unittest.main()
