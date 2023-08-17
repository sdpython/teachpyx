import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools.data_helper import download_and_unzip


class TestDataHelper(ExtTestCase):
    def test_download_and_unzip(self):
        url = "https://github.com/sdpython/teachpyx/raw/paris/_data/paris_54000.zip"
        data = download_and_unzip(url, ".", verbose=True)
        self.assertEqual(data[0], "paris_54000.zip")


if __name__ == "__main__":
    unittest.main(verbosity=2)
