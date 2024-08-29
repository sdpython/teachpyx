# coding: utf-8

###################################
# question 1 : retourner un tableau
###################################

pieces = [1, 2, 5, 10, 20, 50]
pieces.reverse()
print(pieces)  # affiche [50, 20, 10, 5, 2, 1]

# il existait d'autres solutions
pieces.sort(reverse=True)

##################################################################
# question 2 : trouve la plus grande pi�ce inf�rieure � un montant
##################################################################


def plus_grande_piece(montant, pieces):
    # on suppose que les pi�ces sont tri�es par ordre d�croissant

    for p in pieces:
        if p <= montant:
            return p

    # on peut ajouter la ligne
    return 0
    # qui correspond au fait qu'aucune pi�ce plus petite ou �gale au montant
    # n'a �t� trouv� --> le montant est n�gatif ou nul


# on v�rifie
print("plus_grande_piece (80, pieces) =", plus_grande_piece(80, pieces))
# affiche 50

####################################
# question 3 : d�composer un montant
####################################


def decomposer(montant, pieces):
    # on suppose que les pi�ces sont tri�es par ordre d�croissant
    res = []  # contiendra la liste des pi�ces pour le montant
    while montant > 0:
        p = plus_grande_piece(montant, pieces)  # on prend la plus grande pi�ce
        # inf�rieure ou �gale au montant
        res.append(p)  # on l'ajoute � la solution
        montant -= p  # on �t� p � montant :
        # c'est ce qu'il reste encore � d�composer
    return res


print("decomposer (98, pieces) =", decomposer(98, pieces))
# affiche [50, 20, 20, 5, 2, 1]

print("decomposer (99, pieces) =", decomposer(99, pieces))
# affiche [50, 20, 20, 5, 2, 2]

######################################################
# question 4 : trouver la d�composition la plus grande
######################################################


def maximum_piece(pieces):
    # d�termine le nombre maximum de pi�ces � utiliser
    maxi = 0
    montant = 0
    for m in range(1, 100):
        r = decomposer(m, pieces)
        # si on remplace cette ligne par if len (r) > maxi :
        if len(r) >= maxi:
            maxi = len(r)  # on trouve le plus petit montant
            # avec la pire d�composition
            montant = m  # et non le plus grand montant
            # avec la pire d�composation
    return maxi, montant


print("maximum_piece (pieces) =", maximum_piece(pieces))  # affiche (6, 99))

##################################
# question 5 : d�composition de 98
##################################

pieces4 = [1, 2, 4, 5, 10, 20, 50]
pieces4.reverse()

# [50, 20, 20, 5, 2, 1]
print("decomposer (98, pieces) = ", decomposer(98, pieces))
# [50, 20, 20, 5, 2, 1]
print("decomposer (98, pieces4) = ", decomposer(98, pieces4))

"""
Les deux d�compositions sont identiques.
Or il existe une d�composition plus courte avec la pi�ce 4 :
98 = 50 + 20 + 20 + 4 + 4 = 5 pi�ces

L'algorithme fait la m�me erreur lorsqu'il d�compose le montant 8.
Il cherche toujours la plus grande pi�ce inf�rieure au montant qui est 5.
Il lui est alors impossible d'utiliser la pi�ce 4  pour d�composer 8.

Cet algorithme ne fournit pas la bonne solution avec ce nouveau jeu de pi�ces.
"""

#################################
# question 6 : algorithme optimal
#################################

# version r�cursive : tr�s longue


def decomposer_optimal(montant, pieces):
    if montant in pieces:
        return [montant]
    else:
        r = [1 for m in range(montant)]
        for p in pieces:
            if montant > p:
                # si ce test n'est pas fait, la r�currence peut �tre infinie
                # car les montants n�gatifs ne sont pas pris en compte
                # par le premier test
                dec = [*decomposer_optimal(montant - p, pieces), p]
                if len(dec) < len(r):
                    r = dec

        return r


# print("decomposer_optimal (98, pieces4) =", decomposer_optimal (98, pieces4)
# trop long

# version non r�cursive


def decomposer_optimal(montant, pieces):
    memo = [[1 for li in range(m)] for m in range(montant + 1)]
    # memo [i] contient la pire d�composition du montant i (que des pi�ces de un)

    # pour les pi�ces de pieces, on sait faire plus court
    for p in pieces:
        if p < len(memo):
            memo[p] = [p]

    for m in range(1, montant + 1):
        for p in pieces:
            if m > p:
                # on calcule la nouvelle d�composition
                dec = [p] + memo[m - p]
                # si elle est plus courte, on la garde
                if len(dec) < len(memo[m]):
                    memo[m] = dec

    # on retourne la meilleur d�composition pour montant
    return memo[montant]


# beaucoup plus rapide
print("decomposer_optimal (98, pieces4) =", decomposer_optimal(98, pieces4))
# affiche [50, 20, 20, 4, 4]


#######################
# question 7 : r�sultat
#######################


# pour trouver la d�composition la plus longue avec n'importe quel jeu de pi�ces
# on reprend la fonction maximum_piece et on remplace decomposer par decomposer optimale


def maximum_piece(pieces):
    # d�termine le nombre maximum de pi�ces � utiliser
    maxi = 0
    montant = 0
    for m in range(1, 100):
        r = decomposer_optimal(m, pieces)
        # si on remplace cette ligne par if len (r) > maxi :
        if len(r) >= maxi:
            maxi = len(r)  # on trouve le plus petit montant
            # avec la pire d�composation
            montant = m  # et non le plus grand montant
            # avec la pire d�composation
    return maxi, montant


print("maximum_piece (pieces) =", maximum_piece(pieces))  # affiche (6, 99)
print("maximum_piece (pieces4) =", maximum_piece(pieces4))  # affiche (5, 99)


# on teste pour toutes les pi�ces [3,4,6,7,8,9]
# ajout�es au jeu de pi�ces standard [1,2,5,10,20,50]
ensemble = [3, 4, 6, 7, 8, 9]

for ajout in [3, 4, 6, 7, 8, 9]:
    pieces = [1, 2, 5, 10, 20, 50] + [ajout]  # noqa: RUF005
    pieces.sort(reverse=True)
    print("maximum_piece (" + str(pieces) + ") = ", maximum_piece(pieces))

# r�sultat :
"""
maximum_piece ([50, 20, 10, 5, 3, 2, 1]) =  (6, 99)
maximum_piece ([50, 20, 10, 5, 4, 2, 1]) =  (5, 99)  # 4, ok
maximum_piece ([50, 20, 10, 6, 5, 2, 1]) =  (6, 99)
maximum_piece ([50, 20, 10, 7, 5, 2, 1]) =  (5, 99)  # 7, ok
maximum_piece ([50, 20, 10, 8, 5, 2, 1]) =  (5, 99)  # 8, ok
maximum_piece ([50, 20, 10, 9, 5, 2, 1]) =  (5, 98)  # 9, ok
"""


############################
# question 8 : d�composition
############################

"""
On cherche ici le co�t de la fonction decomposer_optimal en fonction du montant.
Il n'y a qu'une seule boucle qui d�pend du montant, le co�t de la fonction est en O(n).

Dans la version r�cursive, le co�t est le r�sultat d'une suite r�currente :
u(n) = u(n-1) + ... + u(n-d)
o� d est le nombre de pi�ces.

Le co�t est donc en O(a^n) o� a est la plus grande des racines du polyn�me :

P (x) = x^d - x^(d-1) - ... - 1

P(1) < 0 et lim P(x) = infini lorsque x tend vers infini,
donc la plus grande des racines est sup�rieure � 1.
Le co�t de la fonction decomposer_optimal r�cursive est en O(a^n) avec 1,96 < a < 1,97.

Pour des explications plus cons�quentes, voir la page
http://fr.wikipedia.org/wiki/Suite_r%C3%A9currente_lin%C3%A9aire
sur les suites r�currentes.
"""
