"""
@brief      test log(time=0s)
"""
import unittest
from teachpyx import check, _setup_hook


class TestInit(unittest.TestCase):

    def test_check(self):
        assert check()
        _setup_hook()


if __name__ == "__main__":
    unittest.main()
