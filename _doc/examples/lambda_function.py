# -*- coding: utf-8 -*-
"""
Astuces avec les lambda functions
=================================

Les `lambda <https://docs.python.org/fr/3/reference/expressions.html?highlight=lambda#lambda>`_
fonctions ont :epkg:`Python` sont assez
plutôt esthétiques si ce n'est le mot-clé ``lambda``
assez long à écrire. A priori l'écrire est équivalent
à celle avec le mot-clé ``def``. On s'en sert parfois aussi
pour réduire le nombre d'arguments d'une fonction pour
en fixer un.
"""


def twoargs(a, b):
    return a + b


def oneargs(x):
    return twoargs(x, 5)


print(oneargs(1))

################
# Et dans une liste, cela donne ce qui suit.

print([oneargs(a) for a in range(0, 3)])

#######################
# Dans le cas présent, cela revient à écrire cela
# ce qui est quand même plus simple.

fcts = [a + 5 for a in range(0, 3)]
print(fcts)

#######################
# Ou encore...

fcts = [oneargs(a) for a in range(0, 3)]
print(fcts)

#######################
# Les lambdas fonctions sont aussi utilisées pour
# retarder l'exécution d'un calcul.
# La première liste définit le calcul dans des
# lambda fonctions. La seconde les exécute.

fcts_a = [lambda: oneargs(a) for a in range(0, 3)]
fcts_b = [f() for f in fcts_a]
print(fcts_b)

#######################
# Le résultat est constant ce qui n'est pas
# celui souhaité. Les valeurs sont constante.
# Les fonctions sont exécutées mais l'argument
# est le même pour tous car elles partagent les
# mêmes variables locales. Au moment de leur
# exécution, la variable a ne change plus de valeur.
# Une solution consiste à conserver chaque valeur
# distincte de a dans une valeur par défaut.

fcts_a = [lambda a=a: oneargs(a) for a in range(0, 3)]
fcts_b = [f() for f in fcts_a]
print(fcts_b)

#########################
# :epkg:`pylint` fait surgir le warning suivant quand cela arrive
# ``W0640: Cell variable v defined in loop``.
