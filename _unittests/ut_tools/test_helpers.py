import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools import total_size


class TestHelpers(ExtTestCase):
    def test_draw_diagram_png(self):
        a = dict(g=4)
        self.assertGreater(total_size(a), 0)

        class A:
            def __init__(self):
                self.f = dict(y="3")

        a = A()
        self.assertGreater(total_size(a), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
