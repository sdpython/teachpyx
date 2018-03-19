"""
@brief      test log(time=4s)
"""

import sys
import os
import unittest
from datetime import datetime


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode.pip_helper import fix_pip_902
from src.teachpyx.faq.faq_python import entier_grande_taille, difference_div, python_path, same_variable, stringio
from src.teachpyx.faq.faq_python import property_example, enumerate_regex_search, sortable_class, list_of_installed_packages
from src.teachpyx.faq.faq_python import information_about_package, get_month_name, get_day_name


class TestFaqMissing (unittest.TestCase):

    def test_faq_pythonm(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        entier_grande_taille()
        difference_div()
        python_path()
        a, b = 1, 1
        same_variable(a, b)
        stringio("e")
        property_example()
        assert list(enumerate_regex_search("r*", "rararr"))
        sortable_class([5, 5])
        fix_pip_902()
        list_of_installed_packages()
        fLOG(information_about_package("pip"))
        self.assertEqual(get_month_name(datetime(2016, 4, 5)), 'April')
        self.assertEqual(get_day_name(datetime(2016, 4, 17)), 'Sunday')


if __name__ == "__main__":
    unittest.main()
