import unittest
import os
import sys
import importlib
import shutil
import subprocess
import time
import warnings
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
        raise RuntimeError(
            f"Unable to find or execute {module_name!r} in {module_file_path!r}."
        )
    module = importlib.util.module_from_spec(module_spec)
    return module_spec.loader.exec_module(module)


class TestDocumentationNotebook(ExtTestCase):
    _tmp = "temp_notebooks"

    def post_process(self, content):
        lines = []
        for line in content.split("\n"):
            if "get_ipython()" in line:
                line = "# " + line
            lines.append(line)
        return "\n".join(lines)

    def run_test(self, nb_name: str, verbose=0) -> int:
        ppath = os.environ.get("PYTHONPATH", "")
        if len(ppath) == 0:
            os.environ["PYTHONPATH"] = ROOT
        elif ROOT not in ppath:
            sep = ";" if sys.platform == "win32" else ":"
            os.environ["PYTHONPATH"] = ppath + sep + ROOT

        perf = time.perf_counter()

        exporter = PythonExporter()
        content = self.post_process(exporter.from_filename(nb_name)[0])
        bcontent = content.encode("utf-8")

        tmp = self._tmp
        if not os.path.exists(tmp):
            os.mkdir(tmp)
        # with tempfile.NamedTemporaryFile(suffix=".py") as tmp:
        name = os.path.splitext(os.path.split(nb_name)[-1])[0]
        if os.path.exists(tmp):
            tmp_name = os.path.join(tmp, name + ".py")
            self.assertEndsWith(tmp_name, ".py")
            with open(tmp_name, "wb") as f:
                f.write(bcontent)

            fold, name = os.path.split(tmp_name)

            try:
                mod = import_source(fold, os.path.splitext(name)[0])
                assert mod is not None
            except (FileNotFoundError, RuntimeError):
                # try another way
                cmds = [sys.executable, "-u", tmp_name]
                p = subprocess.Popen(
                    cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                res = p.communicate()
                _out, err = res
                st = err.decode("ascii", errors="ignore")
                if "No such file or directory" in st:
                    raise FileNotFoundError(st)  # noqa: B904
                if len(st) > 0 and "Traceback" in st:
                    msg = (
                        f"Example {nb_name!r} (cmd: {cmds} - "
                        f"exec_prefix={sys.exec_prefix!r}) "
                        f"failed due to\n{st}"
                    )
                    if "CERTIFICATE_VERIFY_FAILED" in st and sys.platform == "win32":
                        warnings.warn(msg, stacklevel=0)
                    else:
                        raise AssertionError(msg)  # noqa: B904

        dt = time.perf_counter() - perf
        if verbose:
            print(f"{dt:.3f}: run {name!r}")
        return 1

    @classmethod
    def add_test_methods_path(cls, fold, copy_folder=None):
        if copy_folder:
            full_path = os.path.join(fold, copy_folder)
            assert os.path.exists(full_path), f"Unable to find {full_path!r}"
            dest = copy_folder
            if not os.path.exists(dest):
                os.makedirs(dest)
            for name in os.listdir(full_path):
                if not os.path.exists(os.path.join(dest, name)):
                    shutil.copy(os.path.join(full_path, name), dest)

        found = os.listdir(fold)
        last = os.path.split(fold)[-1]
        for name in found:
            if name.endswith(".ipynb"):
                fullname = os.path.join(fold, name)
                reason = None
                if not reason and (
                    "interro_rapide_" in name
                    or (
                        sys.platform == "win32"
                        and (
                            "protobuf" in name
                            or "td_note_2021" in name
                            or "nb_pandas" in name
                        )
                    )
                ):
                    reason = "protobuf on windows not working"
                if not reason and "seance5_algo2" in name:
                    reason = "profiling not working on CI"
                if (
                    not reason
                    and "module_file_regex" in name
                    and sys.platform != "win32"
                ):
                    reason = "regex not working on windows"
                if not reason and (
                    "ml_a_tree_overfitting" in name
                    and os.environ.get("CIRCLECI", "undefined") != "undefined"
                ):
                    reason = "tree_overfitting too long"
                if not reason and "pretraitement_son" in name:
                    reason = "audio too long"
                if not reason and "ml_ml_features_model" in name:
                    reason = "http request denied"

                if reason:

                    @unittest.skip(reason)
                    def _test_(self, fullname=fullname):
                        res = self.run_test(fullname, verbose=VERBOSE)
                        self.assertIn(res, (-1, 1))

                else:

                    def _test_(self, fullname=fullname):
                        res = self.run_test(fullname, verbose=VERBOSE)
                        self.assertIn(res, (-1, 1))

                lasts = last.replace("-", "_")
                names = os.path.splitext(name)[0].replace("-", "_")
                setattr(cls, f"test_{lasts}_{names}", _test_)

    @classmethod
    def add_test_methods(cls):
        this = os.path.abspath(os.path.dirname(__file__))
        folds = [
            os.path.join(this, "..", "..", "_doc", "c_data"),
            os.path.join(this, "..", "..", "_doc", "practice", "algo-base"),
            os.path.join(this, "..", "..", "_doc", "practice", "algo-compose"),
            os.path.join(this, "..", "..", "_doc", "practice", "exams"),
            os.path.join(this, "..", "..", "_doc", "practice", "ml"),
            os.path.join(this, "..", "..", "_doc", "practice", "py-base"),
            os.path.join(this, "..", "..", "_doc", "practice", "tds-base"),
            os.path.join(this, "..", "..", "_doc", "practice", "years", "2023"),
            os.path.join(this, "..", "..", "_doc", "practice", "years", "2025"),
        ]
        for fold in folds:
            cls.add_test_methods_path(
                os.path.normpath(fold),
                copy_folder=("images" if fold.endswith(("ml", "py-base")) else None),
            )


TestDocumentationNotebook.add_test_methods()

if __name__ == "__main__":
    unittest.main(verbosity=2)
