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
# Il est possible de corriger le tir avec l'argument `dropna`.


df.groupby("a", dropna=False).sum()
