# coding: utf-8
"""

.. _burrowswheelerrst:

==============================
Transformée de Burrows Wheeler
==============================

La transformée de `Burrows-Wheeler
<https://fr.wikipedia.org/wiki/Transform%C3%A9e_de_Burrows-Wheeler>`_
transforme un mot en un autre mot composée des mêmes lettres
mais aux propriétés statistiques différentes.
Les deux fonctions qui suivent implémentent les algorithmes
décrits sur la page Wikipedia.

Codage
======
"""


def code_burrows(text: str) -> str:
    # étape 1: matrice décalée
    decalages = ["".join(text[i:] + text[:i]) for i in range(len(text))]
    # étape 2: tri
    decalages.sort()
    # on cherche la position du mot initial
    pos = decalages.index(text)
    # fin
    return pos, "".join(decalages[i][-1] for i in range(len(text)))


print(code_burrows("ENSAE"))

############################################
# Décodage
# ========


def decode_burrows(pos, last_col):
    first_col = sorted(last_col)
    two_cols = list(zip(last_col, first_col))
    for _i in range(2, len(last_col)):
        two_cols.sort()
        two_cols = [(c, *t) for c, t in zip(last_col, two_cols)]
    two_cols.sort()
    return "".join(two_cols[pos])


print(decode_burrows(2, "SAEEN"))

##############################
# On vérifie que le code vérifie des tests unitaires simples.


def test_burrows():
    for mot in ["AA", "AB", "BA", "ABC", "ACB", "BCA", "BAC", "ENSAE"]:
        pos, code = code_burrows(mot)
        decode = decode_burrows(pos, code)
        assert (
            decode == mot
        ), f"problème avec {mot}, decode={decode}, pos={pos}, code={code}"


test_burrows()
