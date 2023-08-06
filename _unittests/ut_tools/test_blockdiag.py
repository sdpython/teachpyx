import unittest
from PIL import Image
from teachpyx.ext_test_case import ExtTestCase, ignore_warnings
from teachpyx.tools import draw_diagram


class TestBlockDiag(ExtTestCase):
    @ignore_warnings(DeprecationWarning)
    def test_draw_diagram_png(self):
        code = """
            blockdiag {
                A -> B -> C -> D;
                A -> E -> F -> G;
            }
            """.replace(
            "            ", ""
        )
        img = draw_diagram(code, fmt="png")
        self.assertNotEmpty(img)

    @ignore_warnings(DeprecationWarning)
    def test_draw_diagram_pillow(self):
        code = """
            blockdiag {
                A -> B -> C -> D;
                A -> E -> F -> G;
            }
            """.replace(
            "            ", ""
        )
        img = draw_diagram(code, fmt="pillow")
        self.assertTrue(img, Image)
        self.assertEqual(img.size, (832, 200))

    @ignore_warnings(DeprecationWarning)
    def test_draw_diagram_svg(self):
        code = """
            blockdiag {
                A -> B -> C -> D;
                A -> E -> F -> G;
            }
            """.replace(
            "            ", ""
        )
        img = draw_diagram(code, fmt="svg")
        self.assertTrue(img, str)
        self.assertTrue(
            '<rect fill="rgb(0,0,0)" height="40" stroke="rgb(0,0,0)"' in img
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
