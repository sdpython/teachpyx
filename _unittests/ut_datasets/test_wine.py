import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.datasets import load_wine_dataset


class TestWine(ExtTestCase):

    def test_wines_download(self):
        df = load_wine_dataset(download=True)
        self.assertEqual(df.shape, (178, 14))

    def test_wines_local(self):
        df = load_wine_dataset(download=False)
        self.assertEqual(df.shape, (178, 14))


if __name__ == "__main__":
    unittest.main()
