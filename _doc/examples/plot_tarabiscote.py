# coding: utf-8
"""
====================================
Exercices expliqués de programmation
====================================

Quelques exercices autour de la copie de liste, du temps de calcul, de l'héritage.

Copie de listes
===============

La fonction ``somme`` est censée faire la concaténation de toutes les
listes contenues dans ``ens``. Le résultat retourné est effectivement 
celui désiré mais la fonction modifie également la liste ``ens``, pourquoi ?
"""
import math
import copy
import numpy


def somme(tab):
    li = tab[0]
    for i in range(1, len(tab)):
        li += tab[i]
    return li


ens = [[0, 1], [2, 3]]
print(somme(ens))
print(ens)


########################################
# Le problème vient du fait qu'une affectation en *python*
# (seconde ligne de la fonction ``somme`` ne fait pas une copie
# mais crée un second identificateur pour désigner la même chose.
# Ici, ``l`` et ``tab[0]`` désignent la même liste, modifier l'une
# modifie l'autre. Ceci explique le résultat. Pour corriger,
# il fallait faire une copie explicite de ``tab[0]`` :


def somme(tab):
    li = copy.copy(tab[0])  ###### ligne modifiée
    for i in range(1, len(tab)):
        li += tab[i]
    return li


ens = [[0, 1], [2, 3]]
print(somme(ens))
print(ens)


########################################
# Il était possible, dans ce cas, de se passer de copie en écrivant :


def somme(tab):
    li = []  ###### ligne modifiée
    for i in range(0, len(tab)):  ###### ligne modifiée
        li += tab[i]
    return li


ens = [[0, 1], [2, 3]]
print(somme(ens))
print(ens)


########################################
# Erreur de logique
# =================
#
# Le programme suivant fonctionne mais le résultat n'est pas celui escompté.


li = ["un", "deux", "trois", "quatre", "cinq"]

for i in range(0, len(li)):
    mi = i
    for j in range(i, len(li)):
        if li[mi] < li[j]:
            mi = j
    e = li[i]
    li[mi] = li[i]
    li[i] = e

li


########################################
# Ce programme est censé effectuer un tri par ordre alphabétique
# **décroissant**. Le problème intervient lors de la permutation de
# l'élément ``l[i]`` avec l'élément ``l[mi]``. Il faut donc écrire :


li = ["un", "deux", "trois", "quatre", "cinq"]
for i in range(0, len(li)):
    mi = i
    for j in range(i, len(li)):
        if li[mi] < li[j]:
            mi = j
    e = li[mi]  ######## ligne modifiée
    li[mi] = li[i]
    li[i] = e

li


########################################
# Coût d'un algorithme
# ====================
#
# Le coût d'un algorithme ou d'un programme est le nombre d'opérations
# (additions, multiplications, tests, ...) qu'il effectue. Il s'exprime
# comme un multiple d'une fonction de la dimension des données que
# le programme manipule. Par exemple : :math:`O(n)`,
# :math:`O(n^2)`, :math:`O(n\ln n)`, ...


def moyenne(tab):
    s = 0.0
    for x in tab:
        s += x
    return s / len(tab)


def variance(tab):
    s = 0.0
    for x in tab:
        t = x - moyenne(tab)
        s += t * t
    return s / len(tab)


li = [0, 1, 2, 2, 3, 1, 3, 0]
print(moyenne(li))
print(variance(li))


########################################
# Tout d'abord, le coût d'un algorithme est très souvent exprimé comme un
# multiple de la dimension des données qu'il traite. Ici, la dimension
# est la taille du tableau ``tab``. Par exemple, si on note ``n = len(tab)``,
# alors le coût de la fonction ``moyenne`` s'écrit :math:`O(n)` car cette
# fonction fait la somme des *n* éléments du tableau.
#
# La fonction ``variance`` contient quant à elle un petit piège. Si elle
# contient elle aussi une boucle, chacun des $n$ passages dans cette boucle
# fait appel à la fonction ``moyenne``. Le coût de la fonction ``variance`` est donc
# :math:`O(n^2)`.
#
# Il est possible d'accélérer le programme car la fonction ``moyenne``
# retourne le même résultat à chaque passage dans la boucle.
# Il suffit de mémoriser son résultat dans une variable avant d'entrer
# dans la boucle comme suit :


def variance(tab):
    s = 0.0
    m = moyenne(tab)
    for x in tab:
        t = x - m
        s += t * t
    return s / len(tab)


variance(li)


########################################
# Le coût de la fonction ``variance`` est alors :math:`O(n)`.
#
# Le coût d'un algorithme peut être évalué de manière plus précise et
# nécessiter un résultat comme $n^2 + 3n + 2$ mais cette exigence est
# rarement utile pour des langages comme *python*. L'expression
# ``for x in tab:`` cache nécessairement un test qu'il faudrait prendre en
# compte si plus de précision était exigée. Il faudrait également se
# tourner vers un autre langage de programmation, plus précis dans sa syntaxe.
# Par exemple, lorsqu'on conçoit un programme avec le langage C ou C++,
# à partir du même code informatique, on peut construire deux programmes
# exécutables. Le premier (ou version *debug*), lent, sert à la mise au point :
# il inclut des tests supplémentaires permettant de vérifier à chaque étape
# qu'il n'y a pas eu d'erreur (une division par zéro par exemple).
# Lorsqu'on est sûr que le programme marche, on construit la seconde version
# (ou *release*), plus rapide, dont ont été ôtés tous ces tests de
# conception devenus inutiles.
#
# *python* aboutit à un programme lent qui inclut une quantité de tests
# invisibles pour celui qui programme mais qui détecte les erreurs plus vite
# et favorise une conception rapide. Il n'est pas adapté au traitement
# d'information en grand nombre et fait une multitude d'opérations cachées.
#
# Héritage double
# ===============
#
# On a besoin dans un programme de créer une classe ``carre`` et une classe
# ``rectangle``. Mais on ne sait pas quelle classe doit hériter de l'autre.
# Dans le premier programme, ``rectangle`` hérite de ``carre``.


class carre:
    def __init__(self, a):
        self.a = a

    def surface(self):
        return self.a**2


class rectangle(carre):
    def __init__(self, a, b):
        carre.__init__(self, a)
        self.b = b

    def surface(self):
        return self.a * self.b


rectangle(3, 4).surface()


########################################
# Dans le second programme, c'est la classe ``carre``
# qui hérite de la classe ``rectangle``.


class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def surface(self):
        return self.a * self.b


class carre(rectangle):
    def __init__(self, a):
        rectangle.__init__(self, a, a)

    def surface(self):
        return self.a**2


carre(3).surface()


########################################
# * Dans le second programme, est-il nécessaire de redéfinir
#   la méthode ``surface`` dans la classe ``carre`` ?
# * Quel est le sens d'héritage qui vous paraît le plus censé,
#   ``class  rectangle(carre)`` ou ``class  carre(rectangle)`` ?
# * On désire ajouter la classe ``losange``. Est-il plus simple que
#   ``rectangle`` hérite de la classe ``carre`` ou l'inverse pour introduire
#   la classe ``losange`` ? Quel ou quels attributs supplémentaires
#   faut-il introduire dans la classe ``losange`` ?

# Le principe de l'héritage est qu'une classe ``carre`` héritant de la classe
# ``rectangle`` hérite de ses attributs et méthodes. L'aire d'un carré est
# égale à celle d'un rectangle dont les côtés sont égaux, par conséquent,
# la méthode ``surface`` de la classe retourne la même valeur que celle de
# la classe ``rectangle``. Il n'est donc pas nécessaire de la redéfinir.
#
# * D'après la réponse de la première question, il paraît plus logique de
#   considérer que ``carre`` hérite de ``rectangle``.
# * Un losange est défini par un côté et un angle ou un côté et la longueur
#   d'une de ses diagonales, soit dans les deux cas, deux paramètres.
#   Dans la première question, il paraissait plus logique que la classe
#   la plus spécifique hérite de la classe la plus générale afin de bénéficier
#   de ses méthodes. Pour introduire le losange, il paraît plus logique de
#   partir du plus spécifique pour aller au plus général afin que chaque
#   classe ne contienne que les informations qui lui sont nécessaires.


class carre:
    def __init__(self, a):
        self.a = a

    def surface(self):
        return self.a**2


class rectangle(carre):
    def __init__(self, a, b):
        carre.__init__(self, a)
        self.b = b

    def surface(self):
        return self.a * self.b


class losange(carre):
    def __init__(self, a, theta):
        carre.__init__(self, a)
        self.theta = theta

    def surface(self):
        return self.a * math.cos(self.theta) * self.a * math.sin(self.theta) * 2


losange(3, 1).surface()


########################################
# Le sens de l'héritage dépend de vos besoins. Si l'héritage porte principalement
# sur les méthodes, il est préférable de partir du plus général pour aller
# au plus spécifique. La première classe sert d'interface pour toutes ses filles.
# Si l'héritage porte principalement sur les attributs, il est préférable de
# partir du plus spécifique au plus général. Dans le cas général, il n'y a pas
# d'héritage plus sensé qu'un autre mais pour un problème donné,
# il y a souvent un héritage plus sensé qu'un autre.
#
# Précision des calculs
# =====================
#
# Voici un aperçu de la précision des calculs pour le calcul :math:`1 - 10^{-n}`.
# L'exercice a pour but de montrer que l'ordinateur ne fait que des calculs approchés
# et que la précision du résultat dépend de la méthode numérique employée.


x = 1.0
for i in range(0, 19):
    x = x / 10
    print(i, "\t", 1.0 - x, "\t", x, "\t", x ** (0.5))


########################################
# Le programme montre que l'ordinateur affiche ``1``
# lorsqu'il calcule :math:`1-10^{-17}`.
# Cela signifie que la précision des calculs en *python*
# est au mieux de :math:`10^{-16}`.
# C'est encore moins bon dans le cas de *float* ou
# réel simple précision codé sur
# 4 octets au lieu de 8 pour les *double*.


x = numpy.float32(1.0)
for i in range(0, 19):
    x = x / numpy.float32(10)
    print(i, "\t", 1.0 - x, "\t", x, "\t", x ** (0.5))


########################################
# On écrit une classe ``matrice_carree_2``
# qui représente une matrice carrée de dimension 2.


class matrice_carree_2:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def determinant(self):
        return self.a * self.d - self.b * self.c


m1 = matrice_carree_2(1.0, 1e-6, 1e-6, 1.0)
m2 = matrice_carree_2(1.0, 1e-9, 1e-9, 1.0)
print(m1.determinant())
print(m2.determinant())


########################################
# La seconde valeur est donc fausse. On considère maintenant la matrice
# :math:`M = \left(\begin{array}{cc} 1 & 10^{-9} \\  10^{-9} & 1 \end{array} \right)`.
#
# On pose :math:`D = \det(M) = 1 - 10^{-18}` et :math:`T = tr(M) = 2`. :math:`\Delta`
# est le déterminant de *M* et *T* sa trace. On sait que les valeurs propres de
# *M* notées :math:`\lambda_1`, :math:`\lambda_2` vérifient :
#
# .. math::
#
#       \begin{array}{lll}
#       D &=& \lambda_1 \lambda_2 \\
#       T &=& \lambda_1 + \lambda_2
#       \end{array}
#
# On vérifie que :math:`(x - \lambda_1)(x - \lambda_2) = x^2 - x
# (\lambda_1 + \lambda_2) + \lambda_1 \lambda_2`.
# Les valeurs propres de $M$ sont donc solutions de l'équation :
# :math:`x^2 - T x + D = 0`.
#
# Le discriminant de ce polynôme est :math:`\Delta = T^2 - 4 D`.
# On peut donc exprimer les valeurs propres de la matrice *M* par :
#
# .. math::
#
#       \begin{array}{lll}
#       \lambda_1 &=& \frac{T - \sqrt{\Delta}}{2} \\
#       \lambda_2 &=& \frac{T + \sqrt{\Delta}}{2}
#       \end{array}
#
# On ajoute donc la méthode suivante à la classe ``matrice_carree_2`` :


class matrice_carree_2:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def determinant(self):
        return self.a * self.d - self.b * self.c

    def valeurs_propres(self):
        det = self.determinant()
        trace = self.a + self.d
        delta = trace**2 - 4 * det
        l1 = 0.5 * (trace - (delta ** (0.5)))
        l2 = 0.5 * (trace + (delta ** (0.5)))
        return l1, l2


m1 = matrice_carree_2(1.0, 1e-6, 1e-6, 1.0)
m2 = matrice_carree_2(1.0, 1e-9, 1e-9, 1.0)
print(m1.valeurs_propres())
print(m2.valeurs_propres())


########################################
# D'après l'énoncé, les valeurs propres de la matrice :math:`M_2` sont les
# sommes de celles de la matrice *I* et de la matrice :math:`M'_2`.
# Par conséquent, ce second calcul mène au résultat suivant :
#
# ::
#
#       l1    = 1-1e-9  = 0.99999999900000002828
#       l2    = 1+ 1e-9 = 1.000000001
#
# La précision des calculs prend sont importance ici. On décompose la matrice
# :math:`M =  \left(\begin{array}{cc} 1 & 0 \\  0 & 1 \end{array}\right) +
# \left(\begin{array}{cc} 0 & 10^{-9} \\  10^{-9} & 0 \end{array}\right) = I + M'`.
#
# On peut démontrer que si $\lambda$ est une valeur propre de :math:`M'`,
# alors :math:`1 + \lambda` est une valeur propre de *M*.
# Que donne le calcul des valeurs propres de $M'$ si on utilise la méthode
# ``valeurs_propres`` pour ces deux matrices ?
#
# On considère maintenant la matrice
# :math:`M'' = \left(\begin{array}{cc} 1 & 10^{-9} \\  -10^{-9} & 1 \end{array}\right)`.
# En décomposant la matrice :math:`M''` de la même manière qu'à la question 4,
# quelles sont les valeurs propres retournées par le programme pour la matrice
# :math:`M''` ? Quelles sont ses vraies valeurs propres ?
#
# La matrice :math:`M''` n'est en fait pas diagonalisable, c'est-à-dire que
# :math:`tr(M'')^2 - 4 \det{M''} = 4 - 4 (1 + 10^{-18}) < 0`.
# Or le calcul proposé par la question 3 aboutit au même résultat faux que pour
# la matrice :math:`M_2`, les deux valeurs propres trouvées seront égales à 1.
# Si on applique la décomposition proposée :
# :math:`M'' = I + \left(\begin{array}{cc}0&-10^{-9}\\
# 10^{-9}&0\end{array}\right) = I + N''`.
# Le programme calcule sans erreur le discriminant négatif de la matrice :math:`N''`
# qui n'est pas diagonalisable. Il est donc impossible d'obtenir des valeurs
# propres réelles pour la matrice :math:`M''` avec cette seconde méthode.
# Cette question montre qu'une erreur d'approximation peut rendre une
# matrice diagonalisable alors qu'elle ne l'est pas. Il faut bien choisir
# cette précision en fonction de la destination des calculs.
