# coding: utf-8
"""
=================
Pandas et groupby
=================
 
Petit tour de passe passe autour d'un :meth:`pandas.DataFrame.groupby`
et des valeurs manquantes qui ne sont plus prises en compte
depuis les dernières versions.

groupby et valeur manquantes
============================
"""


import pandas
from pandas_streaming.df import pandas_groupby_nan


data = [{"a": 1, "b": 2}, {"a": 10, "b": 20}, {"b": 3}, {"b": 4}]
df = pandas.DataFrame(data)
df


########################################
#

df.groupby("a").sum()


########################################
# Les valeurs manquantes ont disparu et c'est le comportement attendu
# d'après `groupby and missing values
# <http://pandas-docs.github.io/pandas-docs-travis/groupby.html#na-and-nat-group-handling>`_.
# Il est possible de ocrriger le tir avec la fonction implémenté dans ce module.


pandas_groupby_nan(df, "a").sum()


########################################
# L'astuce consiste à remplacer les valeurs manquantes par
# d'autres non utilisées dans le dataframe,
# à grouper, puis à leur redonner leur valeurs initiales.
# Le code de la fonction n'est pas très propre car il modifie des
# variables que l'utilisateur n'est pas censé modifier.
# Il est possible que la fonction "casse" pour des versions ultérieures.
# Le `code <https://github.com/sdpython/pandas_streaming/blob/main/
# pandas_streaming/df/dataframe_helpers.py#L301>`_
# utilise quelques variables non documentation du module :epkg:`pandas`.
