"""
@brief      test log(time=0s)
"""

import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8


class TestCodeStyle(unittest.TestCase):

    def test_code_style_src(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'W0212', 'W0107', 'C0415', 'C0209'),
                   skip=['construction_classique.py:577: C0200',
                         "Redefining built-in 'format'",
                         "data_bikes.py:1: F0002"])

    def test_code_style_test(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0111', 'C0103', 'W0622', 'C1801', 'C0412',
                                  'W0122', 'W0123', 'E1101', 'R1705',
                                  'W0703', 'W0107', 'C0415', 'C0209'),
                   skip=["Unused argument 'cell'",
                         ])


if __name__ == "__main__":
    unittest.main()
