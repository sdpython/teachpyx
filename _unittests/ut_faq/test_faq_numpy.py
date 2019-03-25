"""
@brief      test log(time=7s)
"""
import unittest
import math
from teachpyx.faq.faq_numpy import to_float32


class TestFaqNumpy(unittest.TestCase):

    def test_missing(self):
        pi = math.pi
        fpi = to_float32(pi)
        if fpi == pi:
            raise Exception("not possible {0} ? {1}".format(pi, fpi))


if __name__ == "__main__":
    unittest.main()
