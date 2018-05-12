"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
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


from src.teachpyx.examples.numpysex import numpy_matrix2list, numpy_types


class TestNumpys(unittest.TestCase):

    def test_numpys(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import numpy
        exp = [[0, 1, 2], [4, 5, 6]]
        mat = numpy.array(exp)
        lm = numpy_matrix2list(mat)
        self.assertEqual(lm, exp)

    def test_numpys_types(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        dt = numpy_types()
        self.assertEqual(len(dt), 19)


if __name__ == "__main__":
    unittest.main()
