import os
import unittest
import warnings
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools.graphviz_helper import draw_graph_graphviz


class TestGraphviz(ExtTestCase):
    def test_draw_graph_graphviz(self):
        fout = "temp_graphviz_image.png"

        try:
            draw_graph_graphviz(
                [(1, "eee", "red")], [(1, 2, "blue"), (3, 4), (1, 3)], fout
            )
        except FileNotFoundError as e:
            if "No such file or directory: 'dot'" in str(e):
                warnings.warn(str(e))
                return
            raise e

        self.assertTrue(os.path.exists(fout))
        self.assertTrue(os.path.exists(fout + ".gv"))

    def test_draw_graph_graphviz_no_image(self):
        try:
            res = draw_graph_graphviz(
                [(1, "eee", "red")], [(1, 2, "blue"), (3, 4), (1, 3)], image=None
            )
        except FileNotFoundError as e:
            if "No such file or directory: 'dot'" in str(e):
                return
            raise e
        self.assertIn('[label="eee"', res)


if __name__ == "__main__":
    unittest.main(verbosity=2)
