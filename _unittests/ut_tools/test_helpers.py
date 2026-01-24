import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools.helpers import total_size


class TestHelpers(ExtTestCase):
    def test_total_size(self):
        res = total_size([4, (5,), {"r": 5}, {4.5}])
        self.assertGreater(res, 10)


if __name__ == "__main__":
    unittest.main()
