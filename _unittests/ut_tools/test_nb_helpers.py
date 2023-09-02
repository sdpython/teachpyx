import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools.nb_helpers import RenderJsDot


class TestRenderNbJsDot(ExtTestCase):
    def test_render_nb_js_dot(self):
        f = RenderJsDot(dot="digraph{ a -> b; }")
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsDot(dot="digraph{ a -> b; }", only_html=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn("None", out)

    def test_render_nb_js_dot_api(self):
        f = RenderJsDot(dot="digraph{ a -> b; }", only_html=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn("None", out)

    def test_render_nb_js_dot_local(self):
        f = RenderJsDot(dot="digraph{ a -> b; }")
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsDot(dot="digraph{ a -> b; }", only_html=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn("None", out)

    def test_render_nb_js_dot_api_local(self):
        f = RenderJsDot(dot="digraph{ a -> b; }", only_html=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn("None", out)


if __name__ == "__main__":
    unittest.main()
