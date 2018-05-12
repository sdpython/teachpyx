"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import math
from pyquickhelper.loghelper import fLOG


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


from src.teachpyx.faq.faq_numpy import to_float32


class TestFaqNumpy(unittest.TestCase):

    def test_missing(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pi = math.pi
        fpi = to_float32(pi)
        if fpi == pi:
            raise Exception("not possible {0} ? {1}".format(pi, fpi))


if __name__ == "__main__":
    unittest.main()
