import unittest
import math
from teachpyx.faq.faq_numpy import to_float32


class TestFaqNumpy(unittest.TestCase):
    def test_missing(self):
        pi = math.pi
        fpi = to_float32(pi)
        assert abs(fpi - pi) < 1e-7, f"not possible {pi} ? {fpi}"


if __name__ == "__main__":
    unittest.main()
