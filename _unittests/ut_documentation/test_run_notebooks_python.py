# -*- coding: utf-8 -*-
"""
@brief      test log(time=33s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
from pyquickhelper.ipythonhelper import install_python_kernel_for_unittest


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

import src.teachpyx


class TestRunNotebooksPython(unittest.TestCase):

    def test_run_notebook_python(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        kernel_name = None if is_travis_or_appveyor() else install_python_kernel_for_unittest(
            "python3_module_template")

        temp = get_temp_folder(__file__, "temp_run_notebooks_python")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "python"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "_long" not in f and "protobuf" not in f:
                keepnote.append(os.path.join(fnb, f))

        # function to tell that a can be run
        def valid(cell):
            return True

        # additionnal path to add
        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "pyquickhelper", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "jyquickhelper", "src"))
        ]

        # run the notebooks
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths, kernel_name=kernel_name)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.teachpyx)


if __name__ == "__main__":
    unittest.main()
