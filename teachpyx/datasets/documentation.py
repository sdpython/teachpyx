# coding: utf-8
import os
import re
from typing import List, Optional


def root(subfolder: str) -> str:
    "Returns the local folder for all notebooks."
    this = os.path.dirname(__file__)
    if subfolder == "c_data":
        return os.path.abspath(os.path.normpath(os.path.join(this, "..", "..", "_doc")))
    return os.path.abspath(
        os.path.normpath(os.path.join(this, "..", "..", "_doc", "practice"))
    )


def list_notebooks(
    subfolder: str, name: Optional[str] = None, contains: Optional[str] = None
) -> List[str]:
    """
    Retourne les notebooks qui contiennent *name* dans leur nom.

    :param subfolder: sous-répertoire où chercher
    :param name: préfixe à chercher
    :param contains: extrait à chercher
    :return: liste des notebooks (sans répertoire)
    """
    nbs = [os.path.join(root(subfolder), subfolder)]
    nb_ = list(filter(os.path.exists, nbs))
    assert len(nb_) > 0, "Unable to find notebooks in\n{0}".format("\n".join(nbs))
    nb = nb_[0]

    name_ = name
    if name is not None:
        names = [_ for _ in os.listdir(nb) if _.startswith(name_)]
    if contains is not None:
        names = [_ for _ in os.listdir(nb) if contains in _]
    assert len(names) > 0, (
        f"Unable to find any notebook in {nb!r} "
        f"(this file is {__file__}, "
        f"root is {root(subfolder)}, "
        f"sub is {subfolder!r}, name is {name!r})."
    )
    return names


def list_notebooks_rst_links(
    subfolder: str, name: Optional[str] = None, contains: Optional[str] = None
) -> List[str]:
    """
    Retourne une liste de notebooks au format :epkg:`rst`.

    :param subfolder: sous-répertoire où chercher
    :param name: préfixe à chercher
    :param contains: extrait à chercher
    :return: liste des liens
    """

    def _name(s):
        return os.path.splitext(os.path.split(s)[-1])[0]

    def _title(sub, s):
        reg = re.compile("# (.+)")
        fn = os.path.join(root(sub), sub, s)
        assert os.path.exists(fn), (
            f"Unable to find filename {fn!r} (this file is {__file__}, "
            f"root is {root(sub)!r}, sub is {sub!r}, name is {name!r})."
        )
        with open(fn, "r", encoding="utf-8") as f:
            content = f.read()
        f = reg.findall(content)
        assert f, f"File {fn!r} does not have any title."
        title = f[0].strip("\\n\n")
        return title

    names = list_notebooks(subfolder, name, contains)
    prefix = "" if subfolder == "c_data" else "practice-"
    return [
        f":ref:`{_title(subfolder, name)} <nbl-{prefix}{subfolder}-{_name(name)}>`"
        for name in names
    ]
