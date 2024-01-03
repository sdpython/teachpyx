# coding: utf-8
import pandas


def load_enedis_dataset() -> pandas.DataFrame:
    """
    Retourne des données extraites du site :epkg:`Enedis` :
    `Production électrique annuelle par filière à la maille commune
    <https://data.enedis.fr/explore/dataset/production-electrique-par-filiere-a-la-maille-commune/export/>`_.
    Le jeu proposé est un extrait pour les années 2015-2016.
    Notebooks associés à ce jeu de données :

    .. runpython::
        :rst:

        from teachpyx.datasets.documentation import list_notebooks_rst_links
        links = list_notebooks_rst_links("c_data", "enedis")
        links = ["    * %s" % s for s in links]
        print("\\n".join(links))

    :return: :epkg:`pandas:DataFrame`
    """
    url = (
        "https://github.com/sdpython/teachdata/raw/main/enedis/"
        "production-electrique-par-filiere-a-la-maille-commune.extrait.2015-2016.csv.zip"
    )
    df = pandas.read_csv(url, sep=";", encoding="utf-8")
    df["long"] = df["Geo Point 2D"].apply(lambda x: float(x.split(",")[1].strip()))
    df["lat"] = df["Geo Point 2D"].apply(lambda x: float(x.split(",")[0].strip()))
    return df
