import os
from numpy.random import permutation
import pandas
from .data_helper import get_data_folder


__all__ = ["load_wines_dataset"]


def load_wines_dataset(
    download: bool = False, shuffle: bool = False
) -> pandas.DataFrame:
    """
    Retourne le jeu de données
    `wines quality <https://archive.ics.uci.edu/ml/datasets/wine+quality>`_.
    Notebooks associés à ce jeu de données :

    .. runpython::
        :rst:

        from teachpyx.datasets.documentation import list_notebooks_rst_links
        links = list_notebooks_rst_links("ml", "winesr")
        links = ["    * %s" % s for s in links]
        print("\\n".join(links))

    :param download: télécharge le jeu de données ou considères une copie en local.
    :param shuffle: permute aléatoire les données (elles ne le sont pas)
    :return: :class:`pandas.DataFrame`
    """
    if download:
        raise NotImplementedError("Not implemented with the new website.")
        # url = "https://archive.ics.uci.edu/dataset/186/wine+quality.zip"
        # red = pandas.read_csv(url + "winequality-red.csv", sep=";")
        # white = pandas.read_csv(url + "winequality-white.csv", sep=";")
        # red["color"] = "red"
        # white["color"] = "white"
        # df = pandas.concat([red, white])
        # df.columns = [_.replace(" ", "_") for _ in df.columns]
    else:
        fold = get_data_folder()
        data = os.path.join(fold, "wines-quality.csv")
        df = pandas.read_csv(data)
    if shuffle:
        df = df.reset_index(drop=True)
        ind = permutation(df.index)
        df = df.iloc[ind, :].reset_index(drop=True)
    return df


def load_wine_dataset(
    download: bool = False, shuffle: bool = False
) -> pandas.DataFrame:
    """
    Retourne le jeu de données
    `wine quality <https://archive.ics.uci.edu/ml/datasets/wine>`_.
    Notebooks associés à ce jeu de données :

    .. runpython::
        :rst:

        from teachpyx.datasets.documentation import list_notebooks_rst_links
        links = list_notebooks_rst_links("ml", "winesc")
        links = ["    * %s" % s for s in links]
        print("\\n".join(links))

    :param download: télécharge le jeu de données ou considères une copie en local.
    :param shuffle: permute aléatoire les données (elles ne le sont pas)
    :return: :class:`pandas.DataFrame`
    """
    if download:
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        df = pandas.read_csv(url, header=None)
    else:
        fold = get_data_folder()
        data = os.path.join(fold, "wine.data.txt")
        df = pandas.read_csv(data, header=None)
    s = (
        "index Alcohol Malica_cid Ash Alcalinity_of_ash "
        "Magnesium Total_phenols Flavanoids"
    )
    s += " Nonflavanoid_phenols Proanthocyanins Color_intensity Hue"
    s += " OD280_OD315_diluted_wine Proline"
    df.columns = s.split()
    if shuffle:
        df = df.reset_index(drop=True)  # pylint: disable=E1101
        ind = permutation(df.index)
        df = df.iloc[ind, :].reset_index(drop=True)
    return df
