import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools.pandas import read_csv_cached


class TestPandas(ExtTestCase):
    def test_read_csv_cached(self):
        df = read_csv_cached(
            "https://github.com/sdpython/teachpyx/raw/main/_data/paris_54000.zip"
        )
        df2 = read_csv_cached(
            "https://github.com/sdpython/teachpyx/raw/main/_data/paris_54000.zip"
        )
        self.assertEqual(df.shape, df2.shape)
        self.assertEqual(list(df.columns), list(df2.columns))


if __name__ == "__main__":
    unittest.main()
