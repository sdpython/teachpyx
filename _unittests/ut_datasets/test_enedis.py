import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.datasets import load_enedis_dataset


class TestEnedis(ExtTestCase):
    def test_enedis(self):
        df = load_enedis_dataset()
        self.assertEqual(df.shape, (9719, 26))


if __name__ == "__main__":
    unittest.main()
