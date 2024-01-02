import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.datasets import load_wines_dataset


class TestWines(ExtTestCase):
    def test_wines_download(self):
        df = load_wines_dataset(download=True, shuffle=True)
        self.assertEqual(df.shape, (6497, 13))

    def test_wines_local(self):
        df = load_wines_dataset(download=False, shuffle=True)
        self.assertEqual(df.shape, (6497, 13))


if __name__ == "__main__":
    unittest.main()
