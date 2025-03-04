import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.datasets.data_ts import generate_sells


class TestDataTs(ExtTestCase):

    def test_generate_sells(self):
        df = generate_sells()
        self.assertEqual(len(df), 731)


if __name__ == "__main__":
    unittest.main()
