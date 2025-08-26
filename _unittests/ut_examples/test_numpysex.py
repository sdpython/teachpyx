import unittest
import numpy
from teachpyx.examples.numpysex import numpy_matrix2list, numpy_types


class TestNumpys(unittest.TestCase):
    def test_numpys(self):
        exp = [[0, 1, 2], [4, 5, 6]]
        mat = numpy.array(exp)
        lm = numpy_matrix2list(mat)
        self.assertEqual(lm, exp)

    def test_numpys_types(self):
        dt = numpy_types()
        self.assertEqual(len(dt), 17)


if __name__ == "__main__":
    unittest.main()
