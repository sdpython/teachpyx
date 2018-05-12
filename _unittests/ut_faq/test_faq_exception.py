"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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


from src.teachpyx.faq.faq_exception import call_stack


class TestFaqException(unittest.TestCase):

    def test_call_back(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def insidef():
            ft = call_stack()
            return ft

        def insidefe():
            try:
                raise Exception("an error was raised")
            except Exception:
                ft = call_stack()
                return ft

        cb, sb = insidef()
        fLOG(cb, sb)
        self.assertEqual(sb, "")
        self.assertEqual(len(cb), 0)
        cb, sb = insidefe()
        fLOG(cb, sb)
        self.assertEqual(len(cb), 1)
        assert 'raise Exception("an error was raised")' in sb


if __name__ == "__main__":
    unittest.main()
