import unittest
import random
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.practice.tsp_bresenham import draw_line, draw_ellipse


class TestTspBresenham(ExtTestCase):
    def test_bresenham(self):
        x, y = 500, 500
        for _n in range(10):
            x1 = random.randint(0, x - 1)
            y1 = random.randint(0, y - 1)
            x2 = random.randint(0, x - 1)
            y2 = random.randint(0, y - 1)
            ligne1 = draw_line(x1, y1, x2, y2)
            ligne2 = draw_line(x2, y2, x1, y1)
            ligne2.reverse()
            self.assertEqual(len(ligne1), len(ligne2))
            draw_line(x2, y1, x1, y2)
            line = draw_line(x1, y2, x2, y1)
            self.assertIsInstance(line, list)
            self.assertIsInstance(line[0], tuple)

    def test_bresenham_ellipses(self):
        x, y = 500, 500
        for _n in range(10):
            x1 = random.randint(0, x - 1)
            y1 = random.randint(0, y - 1)
            xa = random.randint(50, 100)
            xb = random.randint(50, 100)
            ell = draw_ellipse(x1, y1, xa, xb)
            self.assertIsInstance(ell, list)
            self.assertIsInstance(ell[0], tuple)


if __name__ == "__main__":
    unittest.main(verbosity=2)
