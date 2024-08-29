# coding: utf-8
import urllib2
import math

# question 1


def lit_fichier():
    # le principe est le m�me que pour le chargement d'un fichier
    # le programme lit directement les informations depuis Internet
    f = urllib2.urlopen("???/examen_python/restaurant_paris.txt")
    s = f.read()
    f.close()
    lines = s.split("\n")  # on d�coupe en lignes
    # on d�coupe en colonnes
    lines = [_.strip("\n\r ").split("\t") for _ in lines if len(_) > 0]
    lines = [_ for _ in lines if len(_) == 3]  # on supprime les lignes vides
    # on convertit les coordonn�es en r�el
    lines = [(a[3:], float(b), float(c)) for a, b, c in lines]
    return lines


# question 2


def compte_restaurant(mat):
    # simple comptage, voir le chapitre 3...
    compte = {}
    for cp, _x, _y in mat:
        if cp not in compte:
            compte[cp] = 0
        compte[cp] += 1
    return compte


# question 3


def barycentre(mat):
    # un barycentre est un point (X,Y)
    # o� X et Y sont respectivement la moyenne des X et des Y
    barycentre = {}
    # boucle sur la matrice
    for cp, x, y in mat:
        if cp not in barycentre:
            barycentre[cp] = [0, 0.0, 0.0]
        a, b, c = barycentre[cp]
        barycentre[cp] = [a + 1, b + x, c + y]
    # boucle sur les barycentres
    for cp in barycentre:
        a, b, c = barycentre[cp]
        barycentre[cp] = [b / a, c / a]

    # le co�t de cette fonction est en O (n log k)
    # o� k est le nombre de barycentre
    # de nombreux �l�ves ont deux boucles imbriqu�es,
    # d'abord sur la matrice, ensuite sur les barycentres
    # ce qui donne un co�t en O (nk), beaucoup plus grand
    return barycentre


# question 4


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# question 5


def plus_proche_restaurant(x, y, arr, mat):
    m, mx, my = None, None, None
    for cp, a, b in mat:
        if cp != arr and (m is None or distance(a, b, x, y) < m):
            mx, my = a, b
            m = distance(a, b, x, y)
    return mx, my


# question 6


def densite_approchee(mat):
    g = barycentre(mat)
    compte = compte_restaurant(mat)
    res = {}

    for cp in g:
        out = plus_proche_restaurant(g[cp][0], g[cp][1], cp, mat)
        r = distance(g[cp][0], g[cp][1], out[0], out[1])
        aire = math.pi * r**2
        res[cp] = compte[cp] / aire

    return res


if __name__ == "__main__":
    if False:  # mettre � vrai pour remplacer la fonction plus_proche_restaurant
        # ajout par rapport � l'�nonc�
        # en r�ponse � la derni�re question
        # plut�t que de prendre le premier point � hors de l'arrondissement
        # on consid�re celui correspondant � un quantile (5%)
        # ce qui �vite les quelques restaurants dont les donn�es
        # sont erron�es
        def plus_proche_restaurant_avec_amelioration(x, y, arr, mat):
            all = []
            for cp, a, b in mat:
                if cp != arr:
                    m = distance(a, b, x, y)
                    all.append((m, a, b))
            all.sort()
            a, b = all[len(all) / 20][1:]
            return a, b

        # ajout par rapport � l'�nonc�
        plus_proche_restaurant = plus_proche_restaurant_avec_amelioration

    mat = lit_fichier()
    com = densite_approchee(mat)
    ret = [(v, k) for k, v in com.iteritems()]
    ret.sort()
    for a, b in ret:
        print("%d\t%s" % (a, b))

    # ajout par rapport � l'�nonc�
    # permet de dessiner les restaurants, une couleur par arrondissement
    # on observe que certains points sont aberrants, ce qui r�duit d'autant
    # l'estimation du rayon d'un arrondissement (il suffit qu'un restaurant
    # �tiquet�s dans le 15�me soit situ� pr�s du barycentre du 14�me.)
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = [
        "red",
        "blue",
        "yellow",
        "orange",
        "black",
        "green",
        "purple",
        "brown",
        "gray",
        "magenta",
        "cyan",
        "pink",
        "burlywood",
        "chartreuse",
        "#ee0055",
    ]
    for cp in barycentre(mat):
        lx = [m[1] for m in mat if m[0] == cp]
        ly = [m[2] for m in mat if m[0] == cp]
        c = colors[int(cp) % len(colors)]
        # if cp not in ["02", "20"] : continue
        ax.scatter(lx, ly, s=5.0, c=c, edgecolors="none")
    plt.show()
