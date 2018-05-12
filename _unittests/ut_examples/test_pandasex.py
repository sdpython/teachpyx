"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import pandas
import numpy
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


from src.teachpyx.examples.numpysex import numpy_types
from src.teachpyx.examples.pandasex import pandas_groupby_nan


class TestPandasex(unittest.TestCase):

    def test_pandasex(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        types = [(str, "e"), (int, -10), (float, -20.2),
                 (bytes, bytes("a", "ascii"))]
        skip = (numpy.bool_, numpy.complex64, numpy.complex128)
        types += [(_, _(5)) for _ in numpy_types() if _ not in skip]

        for ty in types:
            data = [{"this": "cst", "type": "tt1=" + str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "tt2=" +
                        str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "row_for_nan"}]
            df = pandas.DataFrame(data)
            gr = pandas_groupby_nan(df, "value")
            co = gr.count()
            li = list(co["value"])
            fLOG("###", li)
            assert numpy.isnan(li[-1])

        for ty in types:
            data = [{"this": "cst", "type": "tt1=" + str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "tt2=" +
                        str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "row_for_nan"}]
            df = pandas.DataFrame(data)
            try:
                gr = pandas_groupby_nan(df, ("value", "this"))
                raise Exception("---")
            except TypeError:
                pass
            try:
                gr = pandas_groupby_nan(df, ["value", "this"])
            except NotImplementedError:
                continue
            co = gr.count()
            li = list(co["value"])
            fLOG("###", li)
            assert numpy.isnan(li[-1])


if __name__ == "__main__":
    unittest.main()
