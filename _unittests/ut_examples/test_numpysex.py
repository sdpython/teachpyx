"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
import numpy
from pandas_streaming.df.dataframe_helpers import numpy_types
from teachpyx.examples.numpysex import numpy_matrix2list


class TestNumpys(unittest.TestCase):

    def test_numpys(self):
        exp = [[0, 1, 2], [4, 5, 6]]
        mat = numpy.array(exp)
        lm = numpy_matrix2list(mat)
        self.assertEqual(lm, exp)

    def test_numpys_types(self):
        dt = numpy_types()
        self.assertEqual(len(dt), 19)


if __name__ == "__main__":
    unittest.main()
