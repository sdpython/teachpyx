# coding: utf-8
"""
Corrélations
============

Dessine les corrélations pour un jeu de données.
"""

from seaborn import clustermap
from teachpyx.datasets import load_wines_dataset

#########################
# Récupération des données

df = load_wines_dataset()
print(df.head(n=2).T)

####################
# Les corrélations avec :epkg:`seaborn`.

clustermap(df.corr(), center=0, cmap="vlag", linewidths=0.75, figsize=(4, 4))

# plt.show()
