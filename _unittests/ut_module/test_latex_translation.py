"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings


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
                "src",)))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor


class TestLatexTranslation(unittest.TestCase):

    def test_translation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            warnings.warn("no pandoc")
            return
        from pyquickhelper.helpgen import latex2rst
        temp = get_temp_folder(__file__, "temp_translation")
        tex = os.path.join(temp, "..", "..", "..", "_todo")
        for t in os.listdir(tex):
            if ".tex" not in t:
                continue
            ft = os.path.join(tex, t)
            to = os.path.join(temp, t.replace(".tex", ".rst"))
            tom = os.path.join(temp, t.replace(".tex", ".rst.tmp"))
            latex2rst(ft, to, encoding="latin-1", fLOG=fLOG, temp_file=tom)


if __name__ == "__main__":
    unittest.main()
