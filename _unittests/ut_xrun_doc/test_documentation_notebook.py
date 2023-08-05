import unittest
import os
import sys
import importlib
import subprocess
import tempfile
import time
from nbconvert import PythonExporter
from teachpyx import __file__ as teachpyx_file
from teachpyx.ext_test_case import ExtTestCase

VERBOSE = 0
ROOT = os.path.realpath(os.path.abspath(os.path.join(teachpyx_file, "..", "..")))


def import_source(module_file_path, module_name):
    if not os.path.exists(module_file_path):
        raise FileNotFoundError(module_file_path)
    module_spec = importlib.util.spec_from_file_location(module_name, module_file_path)
    if module_spec is None:
        raise FileNotFoundError(
            f"Unable to find {module_name!r} in {module_file_path!r}."
        )
    module = importlib.util.module_from_spec(module_spec)
    return module_spec.loader.exec_module(module)


class TestDocumentationNotebook(ExtTestCase):
    def run_test(self, nb_name: str, verbose=0) -> int:
        ppath = os.environ.get("PYTHONPATH", "")
        if len(ppath) == 0:
            os.environ["PYTHONPATH"] = ROOT
        elif ROOT not in ppath:
            sep = ";" if sys.platform == "win32" else ":"
            os.environ["PYTHONPATH"] = ppath + sep + ROOT

        perf = time.perf_counter()

        exporter = PythonExporter()
        content = exporter.from_filename(nb_name)
        bcontent = content[0].encode("utf-8")

        with tempfile.NamedTemporaryFile(suffix=".py") as tmp:
            self.assertEndsWith(tmp.name, ".py")
            tmp.write(bcontent)
            tmp.seek(0)

            fold, name = os.path.split(tmp.name)

            try:
                mod = import_source(fold, os.path.splitext(name)[0])
                assert mod is not None
            except FileNotFoundError:
                # try another way
                cmds = [sys.executable, "-u", os.path.join(fold, name)]
                p = subprocess.Popen(
                    cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                res = p.communicate()
                out, err = res
                st = err.decode("ascii", errors="ignore")
                if len(st) > 0 and "Traceback" in st:
                    raise AssertionError(
                        f"Example {nb_name!r} (cmd: {cmds} - "
                        f"exec_prefix={sys.exec_prefix!r}) "
                        f"failed due to\n{st}"
                    )

        dt = time.perf_counter() - perf
        if verbose:
            print(f"{dt:.3f}: run {name!r}")
        return 1

    @classmethod
    def add_test_methods_path(cls, fold):
        found = os.listdir(fold)
        last = os.path.split(fold)[-1]
        for name in found:
            if name.endswith(".ipynb"):
                fullname = os.path.join(fold, name)

                def _test_(self, name=name):
                    res = self.run_test(fullname, verbose=VERBOSE)
                    self.assertIn(res, (-1, 1))

                setattr(cls, f"test_{last}_{name}", _test_)

    @classmethod
    def add_test_methods(cls):
        this = os.path.abspath(os.path.dirname(__file__))
        fold = os.path.normpath(
            os.path.join(this, "..", "..", "_doc", "practice", "exams")
        )
        cls.add_test_methods_path(fold)


TestDocumentationNotebook.add_test_methods()

if __name__ == "__main__":
    unittest.main(verbosity=2)
