import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.datasets import get_naturalearth_cities, get_naturalearth_lowres


class TestGpdHelper(ExtTestCase):
    def test_get_naturalearth_cities(self):
        filenames = get_naturalearth_cities()
        for filename in filenames:
            self.assertExists(filename)

    def test_get_naturalearth_lowres(self):
        filenames = get_naturalearth_lowres()
        for filename in filenames:
            self.assertExists(filename)


if __name__ == "__main__":
    unittest.main()
