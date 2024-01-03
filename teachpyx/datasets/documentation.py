# coding: utf-8
import os
from typing import List, Optional


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
    this = os.path.dirname(__file__)
    nbs = [
        os.path.abspath(
            os.path.normpath(
                os.path.join(this, "..", "..", "_doc", "practice", subfolder)
            )
        ),
    ]
    nb_ = list(filter(os.path.exists, nbs))
    assert len(nb_) > 0, "Unable to find notebooks in\n{0}".format("\n".join(nbs))
    nb = nb_[0]

    name_ = name
    if name is not None:
        names = [_ for _ in os.listdir(nb) if _.startswith(name_)]
    if contains is not None:
        names = [_ for _ in os.listdir(nb) if contains in _]
    assert len(names) > 0, f"Unable to find any notebook in '{nb}'."
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

    names = list_notebooks(subfolder, name, contains)
    return [f":ref:`nbl-practice-{subfolder}-{_name(name)}`" for name in names]
