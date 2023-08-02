# coding: utf-8
"""
==================================
Points d'implémentation avec numpy
==================================

Quelques écritures efficaces et non efficaces avec :epkg:`numpy`.

accéder à un élément en particulier
===================================
"""
import timeit

import numpy

mat = numpy.zeros((5, 5))
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        mat[i, j] = i * 10 + j
mat


########################################
#


mat[2, 3], mat[2][3]


########################################
#

timeit.timeit("mat[2, 3]", globals=globals(), number=100)


########################################
#

timeit.timeit("mat[2][3]", globals=globals(), number=100)


########################################
# Les deux écritures ont l'air identique puisqu'elle retourne le même résultat.
# Néanmoins, ``mat[2][3]`` crée un tableau temporaire puis extrait un élément.
# Les éléments ne sont pas recopiés mais un objet intermédiaire est créé.


mat[2]
