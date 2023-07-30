"""
@brief      test log(time=4s)
"""
import unittest
import warnings
from datetime import datetime
from pyquickhelper.pycode import ExtTestCase
from teachpyx.faq.faq_python import (
    entier_grande_taille,
    difference_div,
    python_path,
    same_variable,
    stringio,
)
from teachpyx.faq.faq_python import (
    property_example,
    enumerate_regex_search,
    sortable_class,
    list_of_installed_packages,
)
from teachpyx.faq.faq_python import (
    information_about_package,
    get_month_name,
    get_day_name,
)


class TestFaqMissing(ExtTestCase):
    def test_faq_pythonm(self):
        entier_grande_taille()
        difference_div()
        python_path()
        a, b = 1, 1
        same_variable(a, b)
        stringio("e")
        property_example()
        self.assertNotEmpty(list(enumerate_regex_search("r*", "rararr")))
        sortable_class([5, 5])
        self.assertEqual(get_month_name(datetime(2016, 4, 5)), "April")
        self.assertEqual(get_day_name(datetime(2016, 4, 17)), "Sunday")

    def test_faq_pythonm_pip(self):
        try:
            list_of_installed_packages()
        except ImportError as e:
            if "cannot import name 'get_installed_distributions'" in str(e):
                warnings.warn("This should be fixed in a future release.")
            return
        res = information_about_package("pip")
        self.assertNotEmpty(res)


if __name__ == "__main__":
    unittest.main()
