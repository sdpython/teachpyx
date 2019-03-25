"""
@brief      test log(time=7s)
"""
import unittest
import datetime
from teachpyx.faq.faq_python import get_month_name, get_day_name


class TestFaqPython(unittest.TestCase):

    def test_month_name(self):
        dt = datetime.datetime(2016, 1, 25)
        name = get_month_name(dt)
        self.assertEqual(name, "January")

    def test_day_name(self):
        dt = datetime.datetime(2016, 1, 25)
        name = get_day_name(dt)
        self.assertEqual(name, "Monday")


if __name__ == "__main__":
    unittest.main()
