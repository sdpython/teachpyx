# -*- coding: utf-8 -*-
"""
@brief      test log(time=33s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
import teachpyx


class TestRunNotebooksPython(unittest.TestCase):

    def test_run_notebook_python(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_run_notebooks_python")

        # selection of notebooks
        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks", "python"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "_long" not in f and "protobuf" not in f:
                keepnote.append(os.path.join(fnb, f))

        # run the notebooks
        res = execute_notebook_list(temp, keepnote, fLOG=fLOG)
        execute_notebook_list_finalize_ut(res, fLOG=fLOG, dump=teachpyx)


if __name__ == "__main__":
    unittest.main()
