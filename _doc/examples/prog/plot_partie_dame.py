# coding: utf-8
"""

.. _partiedamerst:

================
Parties de dames
================

Exercice de programmation sur les tableaux.

Q1
==

Une partie de dames met en jeu quarante pions, vingt noirs, vingt blancs,
chacun sur des cases différentes. L'objectif est de savoir si un pion est
en mesure d'en prendre un autre. On ne traitera pas le cas des dames.
Chaque pion est défini par :

* deux coordonnées entières, chacune comprise entre 1 et 10
* une couleur, noir ou blanc

On propose deux représentations de l'ensemble de pions :

* Un tableau de 40 pions indicés de 0 à 39 inclus, chaque pion étant défini par :
    * deux coordonnées comprises entre 1 et 10, ou (0,0)
      si le pion n'est plus sur le damier
    * un entier qui vaut 1 pour blanc, 2 pour noir
* Un tableau d'entiers à deux dimensions, chaque case contient :
    * soit 0 s'il n'y a pas de pion
    * soit 1 si la case contient un pion blanc
    * soit 2 si la case contient un pion noir

Y a-t-il d'autres représentations de ces informations ? Si on considère
que l'efficacité d'une méthode est reliée à sa vitesse - autrement dit aux
coûts des algorithmes qu'elles utilisent -, parmi ces deux représentations,
quelle est celle qui semble la plus efficace pour savoir si un pion donné
du damier est en mesure d'en prendre un autre ?

**réponse**

La seconde représentation sous forme de tableau à deux dimensions est
plus pratique pour effectuer les tests de voisinages. Chaque case a
quatre voisines aux quatre coins, il est ensuite facile de déterminer
si ces quatre voisines sont libres ou si elles contiennent un pion.
On sait rapidement le contenu d'une case.

Avec la première représentation - le tableau des pions - pour savoir
s'il existe un pion dans une case voisine, il faut passer en revue
tous les pions pour savoir si l'un d'eux occupe ou non cette case.
Avec la seconde représentation - le tableau à deux dimensions -
on accède directement à cette information sans avoir à la rechercher.
On évite une boucle sur les pions avec la seconde représentation.

Q2
==

Comment représenter un tableau d'entiers à deux dimensions en
langage python à l'aide des types standards qu'il propose,
à savoir t-uple, liste ou dictionnaire ?

**réponse**

Pour représenter le tableau en deux dimensions, il existe trois solutions :

* Une liste de listes, chaque ligne est représentée par une liste.
  Toutes ces listes sont elles-mêmes assemblées dans une liste globale.
* Une seule liste, il suffit de numéroter les cases du damier de 0 à 99,
  en utilisant comme indice pour la case :math:`(i,j)` : :math:`k = 10*i+j`.
  Réciproquement, la case d'indice $k$ aura pour coordonnées
  :math:`(k / 10, \\, k \\% 10)`.
* Un dictionnaire dont la clé est un couple d'entiers.

Q3
==

On cherche à écrire l'algorithme qui permet de savoir si un pion donné
est un mesure de prendre un pion. Quels sont les paramètres
d'entrées et les résultats de cet algorithme ?

**réponse**

On désire savoir si le pion de la case :math:`(i,j)`
peut en prendre un autre. On suppose que le tableau à deux dimensions
est une liste de dix listes appelée ``damier``. ``damier[i][j]``
est donc la couleur du pion de la case :math:`(i,j)`,
à savoir 0 si la case est vide, 1 si le pion est blanc, 2 si le pion est noir.
Pour ces deux derniers cas, la couleur des pions de l'adversaire sera donc
``3 - damier[i][j]``. Les entrées de la fonctions sont donc les indices
``i``, ``j`` et le damier ``damier``. La sortie est une variable booléenne qui
indique la possibilité ou non de prendre. On ne souhaite pas déplacer les pions.

Q4
==

Il ne reste plus qu'à écrire cet algorithme.
"""


def pion_prendre(i, j, damier):
    c = damier[i][j]
    if c == 0:
        return False  # case vide, impossible de prendre
    c = 3 - c  # couleur de l'adversaire

    if damier[i - 1][j - 1] == c:  # s'il y a un pion adverse en haut à gauche
        if damier[i - 2][j - 2] == 0:  # si la case d'après en diagonale est vide
            return True  # on peut prendre

    # on répète ce test pour les trois autres cases
    if damier[i - 1][j + 1] == c and damier[i - 2][j + 2] == 0:
        return True
    if damier[i + 1][j - 1] == c and damier[i + 2][j - 2] == 0:
        return True
    if damier[i + 1][j + 1] == c and damier[i + 2][j + 2] == 0:
        return True

    # si tous les tests ont échoué, on ne peut pas prendre
    return False


damier = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 2, 0, 2],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
]

pion_prendre(2, 2, damier)


########################################
# Voici une fonction équivalente lorsque le damier est un dictionnaire
# dont la clé est un couple d'entiers.


def pion_prendre_dict(i, j, damier):
    c = damier[(i, j)]  # ou encore damier [i,j]
    if c == 0:
        return False  # case vide, impossible de prendre
    c = 3 - c  # couleur de l'adversaire

    # test pour une prise du pion dans les quatre cases voisines
    if damier[i - 1, j - 1] == c and damier[i - 2, j - 2] == 0:
        return True
    if damier[i - 1, j + 1] == c and damier[i - 2, j + 2] == 0:
        return True
    if damier[i + 1, j - 1] == c and damier[i + 2, j - 2] == 0:
        return True
    if damier[i + 1, j + 1] == c and damier[i + 2, j + 2] == 0:
        return True

    # si tous les tests ont échoué, on ne peut pas prendre
    return False


damier_dict = {(i, j): damier[i][j] for i in range(4) for j in range(4)}

print(damier_dict)

pion_prendre_dict(2, 2, damier_dict)


#########################################
#

try:
    pion_prendre_dict(1, 3, damier_dict)
except Exception as e:
    print(e)


##############################################
# Cela ne marche pas très bien, cela laisse supposer que la fonction
# précédente n'est pas très fonctionnelle non plus. Il manque le fait de
# vérifier que les coordonnées testées restent dans l'échiquier.
# La même fonction lorsque le damier est représenté par une seule liste.


def pion_prendre_list(i, j, damier):
    n = int(len(damier) ** 0.5)  # on suppose que le damier est carré
    c = damier[n * i + j]
    if c == 0:
        return False  # case vide, impossible de prendre
    c = 3 - c  # couleur de l'adversaire

    # test pour une prise du pion dans les quatre cases voisines
    if damier[n * (i - 1) + j - 1] == c and damier[n * (i - 2) + j - 2] == 0:
        return True
    if damier[n * (i - 1) + j + 1] == c and damier[n * (i - 2) + j + 2] == 0:
        return True
    if damier[n * (i + 1) + j - 1] == c and damier[n * (i + 2) + j - 2] == 0:
        return True
    if damier[n * (i + 1) + j + 1] == c and damier[n * (i + 2) + j + 2] == 0:
        return True

    return False


damier_list = []
for row in damier:
    damier_list.extend(row)

print(damier_list)

pion_prendre_list(2, 2, damier_list)

###########################################
# Pour ces trois cas, aucun effet de bord n'a été envisagé.
# Si la case est trop près d'un des bords, un des indices
# :math:`i,\;j,\;i-1,\;j-1,\;i+1,\;j+1,\;i-2,\;j-2,\;i+2,\;j+2`
# désignera une case hors du damier. Le code de la fonction
# ``pion_prendre`` devra donc vérifier que chaque case dont elle
# vérifie le contenu appartient au damier.


def pion_prendre_bord(i, j, damier):
    c = damier[i][j]
    if c == 0:
        return False  # case vide, impossible de prendre
    c = 3 - c  # couleur de l'adversaire

    # on répète ce test pour les trois autres cases
    if i >= 2 and j >= 2 and damier[i - 1][j - 1] == c and damier[i - 2][j - 2] == 0:
        return True
    if (
        i >= 2
        and j < len(damier) - 2
        and damier[i - 1][j + 1] == c
        and damier[i - 2][j + 2] == 0
    ):
        return True

    if (
        i < len(damier) - 2
        and j >= 2
        and damier[i + 1][j - 1] == c
        and damier[i + 2][j - 2] == 0
    ):
        return True

    if (
        i < len(damier) - 2
        and j < len(damier) - 2
        and damier[i + 1][j + 1] == c
        and damier[i + 2][j + 2] == 0
    ):
        return True

    return False


pion_prendre_bord(2, 2, damier)


#########################################
#

pion_prendre_bord(1, 3, damier)


#########################################
# La fonction ``pion_prendre(1, 3, damier)`` fonctionne parce que le
# langage python accepte indices négatifs : ``damier[-1][-1]``
# mais le résultat n'est pas nécessairement celui souhaité.
