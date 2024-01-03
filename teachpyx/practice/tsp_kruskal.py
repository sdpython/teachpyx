# coding: utf-8
import functools
import random
import math
from typing import Any, Callable, Dict, List, Optional, Tuple
from .tsp_bresenham import draw_line

POINT = Tuple[float, float]
DISTANCE = Callable[[POINT, POINT], float]
ENSEMBLE = List[POINT]


def construit_ville(n: int, x: int = 1000, y: int = 700):
    """
    Tire aléatoirement *n* villes dans un carrée ``x * y``, on choisit
    ces villes de sortent qu'elles ne soient pas trop proches.
    """
    # deux villes ne pourront pas être plus proches que mind
    mind = math.sqrt(x * x + y * y) / (n * 0.75)
    # liste vide
    lv = []
    while n > 0:
        # on tire aléatoirement les coordonnées d'une ville
        xx = x * random.random()
        yy = y * random.random()
        # on vérifie qu'elle n'est pas trop proche d'aucune autre ville
        ajout = True
        for t in lv:
            d1 = t[0] - xx
            d2 = t[1] - yy
            d = math.sqrt(d1 * d1 + d2 * d2)
            if d < mind:
                ajout = False  # ville trop proche
        # si la ville n'est pas trop proche des autres, on l'ajoute à la liste
        if ajout:
            lv.append((xx, yy))
            n -= 1  # une ville en moins à choisir
    return lv


def distance_euclidian(p1: float, p2: float) -> float:
    """
    Calcule la distance euclienne entre deux villes.
    """
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x * x + y * y)


def vecteur_points(p1: float, p2: float) -> POINT:
    """
    Retourne le vecteur entre les points *p1* et *p2*.
    """
    return (p2[0] - p1[0], p2[1] - p1[1])


def vecteur_norme(vec: POINT) -> float:
    """
    Retourne la norme d'un vecteur.
    """
    return math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])


def vecteur_cosinus(vec1: POINT, vec2: POINT) -> float:
    """
    Retourne le cosinus entre deux vecteurs,
    utilise le produit scalaire.
    """
    norm1 = vecteur_norme(vec1)
    norm2 = vecteur_norme(vec2)
    if norm1 == 0:
        return 1
    if norm2 == 0:
        return 1
    scal = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return scal / (norm1 * norm2)


def vecteur_sinus(vec1: POINT, vec2: POINT) -> float:
    """
    Retourne le sinus entre deux vecteurs,
    utilise le produit vectoriel.
    """
    norm1 = vecteur_norme(vec1)
    norm2 = vecteur_norme(vec2)
    if norm1 == 0:
        return 0
    if norm2 == 0:
        return 0
    scal = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    return scal / (norm1 * norm2)


def oppose_vecteur(vec: POINT) -> POINT:
    """
    retourne le vecteur opposé.
    """
    return (-vec[0], -vec[1])


def repartition_zone(
    villes: ENSEMBLE, zone_taille: float, ask_zone: bool = False
) -> Tuple[Tuple[int, POINT, Tuple[int, int], int], POINT, float, float, float]:
    """
    Répartit les villes en zones, retourne les villes rangées par zones,
    chaque éléments zones [z][k] contient :

    - les coordonnées de la ville
    - ses coordonnées en zone, (zx, zy)
    - son indice dans la liste villes

    La fonction retourne également le nombre de zones
    selon l'axe des abscisses et l'axe des ordonnées,
    retourne aussi le nombre de zones, si *ask_zone* est True,
    retourne un paramètre supplémentaire : *zone*.
    """
    mx = min(v[0] for v in villes)
    my = min(v[1] for v in villes)
    X = max((v[0] - mx) / zone_taille for v in villes)
    Y = max((v[1] - my) / zone_taille for v in villes)
    X = int(X) + 1
    Y = int(Y) + 1

    # attribution des zones
    zone = []
    Zmax = 0
    for i in range(0, len(villes)):
        v = villes[i]
        x = int((v[0] - mx) / zone_taille)
        y = int((v[1] - my) / zone_taille)
        z = int(y * X + x)
        Zmax = max(z, Zmax)
        zone.append((z, v, (x, y), i))

    # rangement par zone
    Zmax += 1
    zones = [[] for i in range(0, Zmax)]
    for z in zone:
        zones[z[0]].append((z[1], z[2], z[3]))

    if ask_zone:
        return zones, X, Y, mx, my, Zmax, zone
    return zones, X, Y, mx, my, Zmax


def voisinage_zone(z: float, Zmax: float, X: float, Y: float) -> List[int]:
    """
    Retourne la liste des voisins d'une zone *z*
    sachant qu'il y a *X* zones sur l'axe des abscisses
    et *Y* zones sur l'axe des ordonnées,
    *Zmax* est le nombre de zones,
    inclus *z* dans cette liste.
    """
    x = z % X
    y = z // X
    voisin_ = [z]
    if x > 0:
        voisin_.append(z - 1)
    if x < X:
        voisin_.append(z + 1)
    if y > 0:
        voisin_.append(z - X)
    if y < Y:
        voisin_.append(z + X)
    if x > 0 and y > 0:
        voisin_.append(z - 1 - X)
    if x > 0 and y < Y:
        voisin_.append(z - 1 + X)
    if x < X and y > 0:
        voisin_.append(z + 1 - X)
    if x < X and y < Y:
        voisin_.append(z + 1 + X)
    voisin = [int(i) for i in voisin_ if Zmax > i >= 0]
    return voisin


def arbre_poids_minimal(
    villes: ENSEMBLE, zone_taille: float, distance: DISTANCE
) -> Dict[str, Any]:
    """
    Construit l'arbre de poids minimal, retourne une liste de
    listes, chaque sous-liste associée à une ville contient la liste des ses voisins,
    *zone_taille* permet de découper l'image en zones,
    les distances ne seront calculées que si
    deux éléments sont dans la même zone ou dans une zone voisine.

    :param villes: list of tuples (tuple = coordinates)
    :param zone_taille: see :func:`repartition_zone`
    :param distance: distance function which returns
        the distance between two elements
    :return: list of lists: each sublist `r[i]`
        contains the indexes of neighbors of node `i` so
        that the whole graph is only one connected component
    """

    def tri_distance(u, v):
        if u[2] < v[2]:
            return -1
        if u[2] > v[2]:
            return 1
        return 0

    rz = repartition_zone(villes, zone_taille=zone_taille)
    zones, X, Y, mx, my, Zmax = rz[:6]

    # calcul des distances
    li = []
    for z in range(0, len(zones)):
        voisin = voisinage_zone(z, Zmax, X, Y)
        for v in zones[z]:
            for zz in voisin:
                for u in zones[zz]:
                    d = distance(v[0], u[0])
                    li.append((v[2], u[2], d))

    # tri
    li = list(sorted(li, key=functools.cmp_to_key(tri_distance)))

    # nombre de composantes connexes
    nb_comp = len(villes)

    # indice de la composante d'une ville
    num_comp = [i for i in range(0, len(villes))]

    # liste des voisins pour chaque ville
    arbre = [[] for i in range(0, len(villes))]

    # liste des villes par composante connexe
    list_comp = [[i] for i in range(0, len(villes))]

    while nb_comp > 1:
        iii = 0
        for c in li:
            iii += 1
            i, j = c[0], c[1]
            if num_comp[i] != num_comp[j]:
                # on relie les villes i et j car elles appartiennent
                # à des composantes connexes différentes
                arbre[i].append(j)  # i est voisine de j
                arbre[j].append(i)  # j est voisine de i
                cl = num_comp[i]  # composante connexe restante
                # composante connexe à agréger à la précédente
                ki = num_comp[j]
                for k in list_comp[ki]:
                    num_comp[k] = cl
                    list_comp[cl].append(k)
                list_comp[ki] = []
                nb_comp -= 1  # une composante connexe en moins

                if nb_comp <= 1:
                    break  # il n'y a plus qu'une seule composante connexe,
                    # inutile de continuer

        if nb_comp > 1:
            # it usually means that zone_taille is too small and some edges
            # we find lost connected components
            # so for these, assuming they are not too many
            # we look for the closest point outside the connected component
            first_count = min(
                (len(li), i) for i, li in enumerate(list_comp) if len(li) > 0
            )
            comp = first_count[1]
            city = list_comp[comp][random.randint(0, len(list_comp[comp]) - 1)]
            # city is not the best choice, just a random one
            dist = min(
                (distance(villes[city], v), i)
                for i, v in enumerate(villes)
                if city != i and num_comp[i] != num_comp[city]
            )
            li = [(city, dist[1])]

    return dict(arbre=arbre, X=X, Y=Y, mx=mx, my=my, Zmax=Zmax)


def circuit_hamiltonien(chemin: List[int]) -> List[int]:
    """
    Extrait un circuit hamiltonien depuis un circuit eulérien,
    passe par tous les sommets une et une seule fois.
    """
    nb = max(chemin) + 1
    res = []
    coche = [False for i in range(0, nb)]
    for c in chemin:
        if coche[c]:
            continue
        res.append(c)
        coche[c] = True
    return res


def equation_droite(p1: POINT, p2: POINT) -> Tuple[float, float, float]:
    """
    retourne l'équation d'une droite passant par p1 et p2,
    ax + by + c = 0, retourne les coefficients a,b,c
    """
    vec = vecteur_points(p1, p2)
    a = vec[1]
    b = -vec[0]
    c = -a * p1[0] - b * p1[1]
    return a, b, c


def evaluation_droite(a: float, b: float, c: float, p: POINT) -> float:
    """
    L'équation d'une droite est : ``ax + by + c``, retourne la valeur
    de cette expression au point *p*.
    """
    return a * p[0] + b * p[1] + c


def intersection_segment(p1: POINT, p2: POINT, p3: POINT, p4: POINT) -> bool:
    """
    Dit si les segments *[p1 p2]* et *[p3 p4]* ont une intersection,
    ne retourne pas l'intersection.
    """
    # équation de la droite (p1 p2)
    a1, b1, c1 = equation_droite(p1, p2)
    a2, b2, c2 = equation_droite(p3, p4)
    s1 = evaluation_droite(a2, b2, c2, p1)
    s2 = evaluation_droite(a2, b2, c2, p2)
    s3 = evaluation_droite(a1, b1, c1, p3)
    s4 = evaluation_droite(a1, b1, c1, p4)
    return s1 * s2 <= 0 and s3 * s4 <= 0


def longueur_chemin(chemin: ENSEMBLE, distance: DISTANCE) -> float:
    """
    Retourne la longueur d'un chemin.
    """
    s = 0
    nb = len(chemin)
    for i in range(0, nb):
        s += distance(chemin[i], chemin[(i + 1) % nb])
    return s


def retournement_essai(
    chemin: ENSEMBLE,
    i: int,
    j: int,
    negligeable: float = 1e-5,
    distance: Optional[DISTANCE] = None,
) -> bool:
    """
    Dit s'il est judicieux de parcourir le chemin entre les sommets *i* et *j*
    en sens inverse, si c'est judicieux, change le chemin et retourne True,
    sinon, retourne False,
    si *j < i*, alors la partie à inverser est
    *i*, *i+1*, *i+2*, ..., *len(chemin)*,
    *-1*, *0*, *1*, ..., *j*.
    """

    nb = len(chemin)
    if i == j:
        return False
    if j - i == -1:
        return False
    if j - i - nb == -1:
        return False

    ia = (i - 1 + nb) % nb
    ja = (j + 1) % nb
    # arcs enlevés
    d_ia_i = distance(chemin[ia], chemin[i])
    d_j_ja = distance(chemin[j], chemin[ja])
    # arcs ajoutés
    d_ia_j = distance(chemin[ia], chemin[j])
    d_i_ja = distance(chemin[i], chemin[ja])
    # amélioration ?
    d = d_ia_j + d_i_ja - d_j_ja - d_ia_i
    if d >= -negligeable:
        return False

    # si amélioration, il faut retourner le chemin entre les indices i et j
    jp = j
    if jp < i:
        jp = j + nb
    ip = i

    while ip < jp:
        i = ip % nb
        j = jp % nb
        ech = chemin[i]
        chemin[i] = chemin[j]
        chemin[j] = ech
        ip = ip + 1
        jp = jp - 1

    return True


def retournement(
    chemin: ENSEMBLE, taille: float, distance: DISTANCE, verbose: int
) -> int:
    """
    Amélioration du chemin par un algorithme simple,
    utilise des retournements de taille au plus <taille>,
    retourne le nombre de modifications.
    """

    # traitement des petits retournements
    nb = len(chemin)
    nb_change = 1
    nbtout = 0
    retour = {}
    while nb_change > 0:
        nb_change = 0
        for t in range(1, taille + 1):
            retour[t] = 0
            for i in range(0, nb):
                j = (i + t) % nb
                b = retournement_essai(chemin, i, j, distance=distance)
                if b:
                    retour[t] += 1
                    nb_change += 1
        nbtout += nb_change
    if verbose > 0:
        print(
            f"nombre de retournements {nbtout} longueur :   \t "
            f"{longueur_chemin(chemin, distance=distance):10.0f} "
            f"--- \t --- : {retour}"
        )
    return nbtout


def echange_position_essai(
    chemin: ENSEMBLE,
    a: int,
    b: int,
    x: float,
    inversion: bool,
    negligeable: float = 1e-5,
    distance: Optional[DISTANCE] = None,
) -> bool:
    """
    Echange la place des villes ka et kb pour les placer entre les villes *i* et *i+1*,
    si inversion est True, on inverse également
    le chemin inséré, si inversion est False,
    on ne l'inverse pas,
    si cela améliore, déplace les villes et retourne True, sinon, retourne False.
    """

    nb = len(chemin)
    xa = (x + 1) % nb
    ka = (a - 1 + nb) % nb
    kb = (b + 1) % nb

    if not inversion:
        if x == ka:
            return False
        if x == kb:
            return False
        if xa == ka:
            return False
        if b < a:
            if a <= x <= b + nb:
                return False
        elif a <= x <= b:
            return False
        if b < a:
            if a <= x + nb <= b + nb:
                return False
        elif a <= x + nb <= b:
            return False

        # arcs enlevés
        d_x_xa = distance(chemin[x], chemin[xa])
        d_ka_a = distance(chemin[ka], chemin[a])
        d_b_kb = distance(chemin[b], chemin[kb])
        # arcs ajoutés
        d_ka_kb = distance(chemin[ka], chemin[kb])
        d_x_a = distance(chemin[x], chemin[a])
        d_b_xa = distance(chemin[b], chemin[xa])

        d = d_ka_kb + d_x_a + d_b_xa - d_x_xa - d_ka_a - d_b_kb
        if d >= -negligeable:
            return False

        # villes à déplacer
        ech = []
        bp = b
        if bp < a:
            bp = b + nb
        for i in range(a, bp + 1):
            ech.append(chemin[i % nb])
        diff = bp - a + 1

        xp = x
        if xp < b:
            xp += nb

        for le in range(b + 1, xp + 1):
            ll = le % nb
            bp = (a + le - b - 1) % nb
            chemin[bp] = chemin[ll]

        for le in range(0, len(ech)):
            chemin[(x + le - diff + 1 + nb) % nb] = ech[le]

        return True

    else:
        if x == ka:
            return False
        if x == kb:
            return False
        if xa == ka:
            return False
        if b < a:
            if a <= x <= b + nb:
                return False
        elif a <= x <= b:
            return False
        if b < a:
            if a <= x + nb <= b + nb:
                return False
        elif a <= x + nb <= b:
            return False

        # arcs enlevés
        d_x_xa = distance(chemin[x], chemin[xa])
        d_ka_a = distance(chemin[ka], chemin[a])
        d_b_kb = distance(chemin[b], chemin[kb])
        # arcs ajoutés
        d_ka_kb = distance(chemin[ka], chemin[kb])
        d_x_b = distance(chemin[x], chemin[b])
        d_a_xa = distance(chemin[a], chemin[xa])

        d = d_ka_kb + d_x_b + d_a_xa - d_x_xa - d_ka_a - d_b_kb
        if d >= -negligeable:
            return False

        # villes à déplacer
        ech = []
        bp = b
        if bp < a:
            bp = b + nb
        for i in range(a, bp + 1):
            ech.append(chemin[i % nb])
        ech.reverse()
        diff = bp - a + 1

        xp = x
        if xp < b:
            xp += nb

        for le in range(b + 1, xp + 1):
            ll = le % nb
            bp = (a + le - b - 1) % nb
            chemin[bp] = chemin[ll]

        for le in range(0, len(ech)):
            chemin[(x + le - diff + 1 + nb) % nb] = ech[le]

        return True


def dessin_arete_zone(
    chemin: ENSEMBLE, taille_zone: float, X: POINT, Y: POINT
) -> List[List[List[int]]]:
    """
    Retourne une liste de listes de listes,
    ``res[i][j]`` est une liste des arêtes passant près de la zone ``(x,y) = [i][j]``,
    si *k* in ``res[i][j]``, alors l'arête *k*, *k+1* est dans la zone *(i,j)*,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur du côté du carré d'une zone.
    """
    res = [[[] for j in range(0, Y + 1)] for i in range(0, X + 1)]
    nb = len(chemin)
    mx = min(_[0] for _ in chemin)
    my = min(_[1] for _ in chemin)
    for i in range(0, nb):
        a = chemin[i]
        b = chemin[(i + 1) % nb]
        x1, x2 = int((a[0] - mx) // taille_zone), int((b[0] - mx) // taille_zone)
        y1, y2 = int((a[1] - my) // taille_zone), int((b[1] - my) // taille_zone)
        line = draw_line(x1, y1, x2, y2)
        for x, y in line:
            res[x][y].append(i)
    return res


def voisinage_zone_xy(x: float, y: float, X: float, Y: float) -> ENSEMBLE:
    """
    Retourne la liste des voisins d'une zone *(x,y)*
    sachant qu'il y a *X* zones sur l'axe des abscisses
    et *Y* zones sur l'axe des ordonnées,
    inclus *z* dans cette liste
    """
    voisin = [(x, y)]
    if x > 0:
        voisin.append((x - 1, y))
    if x < X - 1:
        voisin.append((x + 1, y))
    if y > 0:
        voisin.append((x, y - 1))
    if y < Y - 1:
        voisin.append((x, y + 1))
    if x > 0 and y > 0:
        voisin.append((x - 1, y - 1))
    if x > 0 and y < Y - 1:
        voisin.append((x - 1, y + 1))
    if x < X - 1 and y > 0:
        voisin.append((x + 1, y - 1))
    if x < X - 1 and y < Y - 1:
        voisin.append((x + 1, y + 1))
    return voisin


def echange_position(
    chemin: ENSEMBLE,
    taille: float,
    taille_zone: float,
    X: float,
    Y: float,
    grande: float = 0.5,
    distance: Optional[DISTANCE] = None,
    verbose: int = 0,
) -> int:
    """
    Regarde si on ne peut pas déplacer un segment de longueur taille
    pour supprimer les arêtes les plus longues,
    au maximum <grande> longues arêtes,
    retourne le nombre de changement effectués,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur d'un côté du carré d'une zone.
    """

    nb = len(chemin)

    def tri_arete(x, y):
        """pour trier la liste l par ordre décroissant"""
        if x[2] < y[2]:
            return 1
        if x[2] > y[2]:
            return -1
        return 0

    tmx = min(v[0] for v in chemin)
    tmy = min(v[1] for v in chemin)

    # list des arêtes triés par ordre décroissant
    la = []
    for i in range(0, nb):
        im = (i + 1) % nb
        la.append((i, im, distance(chemin[i], chemin[im])))
    la = list(sorted(la, key=functools.cmp_to_key(tri_arete)))

    # zone associée à chaque arête
    zone = dessin_arete_zone(chemin, taille_zone, X, Y)

    dseuil = la[int(nb * grande)][2]
    nbtout = 0
    nb_change = 0
    iarete = 0
    retour = {}
    for t in range(1, taille + 1):
        retour[t] = 0

    while iarete < nb:
        nb_change = 0
        arete = la[iarete]
        iarete += 1
        x = arete[0]
        xm = arete[1]
        a = chemin[x]
        b = chemin[xm]
        d = distance(a, b)
        if d < dseuil:
            break  # arête trop petite

        # zone traversée par la ligne
        x1, x2 = (int((a[0] - tmx) // taille_zone), int((b[0] - tmx) // taille_zone))
        y1, y2 = (int((a[1] - tmy) // taille_zone), int((b[1] - tmy) // taille_zone))
        ens = draw_line(x1, y1, x2, y2)
        ville = []
        for k, le in ens:
            voisin = voisinage_zone_xy(k, le, X, Y)
            for u, v in voisin:
                ville.extend(zone[u][v])

        # on supprime les doubles
        ville.sort()
        if len(ville) == 0:
            continue
        sup = []
        mx = -1
        for v in ville:
            if v == mx:
                sup.append(v)
            mx = v
        for s in sup:
            ville.remove(s)

        # on étudie les possibilités de casser l'arête (x,xm) aux alentours des villes
        # comprise dans l'ensemble ville
        for t in range(1, taille + 1):
            for i in ville:
                # on essaye d'insérer le sous-chemin (x- t + 1 + nb)  --> x
                # au milieu de l'arête i,i+1
                b = echange_position_essai(
                    chemin, (x - t + 1 + nb) % nb, x, i, False, distance=distance
                )
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue

                # on essaye d'insérer le sous-chemin (xm+ t - 1)  --> xm
                # au milieu de l'arête i,i+1
                b = echange_position_essai(
                    chemin, (xm + t - 1) % nb, xm, i, False, distance=distance
                )
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue

                # on essaye de casser l'arête x,xm en insérant
                # le sous-chemin i --> (i+t) % nb
                b = echange_position_essai(
                    chemin, i, (i + t) % nb, x, False, distance=distance
                )
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue
                # idem
                b = echange_position_essai(
                    chemin, i, (i + t) % nb, x, True, distance=distance
                )
                if b:
                    retour[t] += 1
                    nb_change += 1
                    continue
                # idem
                b = echange_position_essai(
                    chemin, (i - t + nb) % nb, i, x, False, distance=distance
                )
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue
                # idem
                b = echange_position_essai(
                    chemin, (i - t + nb) % nb, i, x, True, distance=distance
                )
                if b:
                    retour[t] += 1
                    nb_change += 1
                    continue

        nbtout += nb_change

    if verbose > 0:
        print(
            f"nombre de déplacements {nbtout} longueur :   \t "
            f"{longueur_chemin(chemin, distance=distance):10.0f} "
            f"--- \t --- : {retour}"
        )
    return nbtout


def supprime_croisement(
    chemin: ENSEMBLE,
    taille_zone: float,
    X: float,
    Y: float,
    distance: Optional[DISTANCE] = None,
    verbose: int = 0,
) -> int:
    """
    Supprime les croisements d'arêtes,
    retourne le nombre de changement effectués,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur d'un côté du carré d'une zone
    """

    nb = len(chemin)
    tmx = min(v[0] for v in chemin)
    tmy = min(v[1] for v in chemin)

    # zone associée à chaque arête
    zone = dessin_arete_zone(chemin, taille_zone, X, Y)
    nbtout = 0

    for i in range(0, nb):
        im = (i + 1) % nb
        a = chemin[i]
        b = chemin[im]

        # zone traversée par la ligne
        x1, x2 = (int((a[0] - tmx) // taille_zone), int((b[0] - tmx) // taille_zone))
        y1, y2 = (int((a[1] - tmy) // taille_zone), int((b[1] - tmy) // taille_zone))
        ens = draw_line(x1, y1, x2, y2)
        ville = []
        for k, le in ens:
            voisin = voisinage_zone_xy(k, le, X, Y)
            for u, v in voisin:
                ville.extend(zone[u][v])

        # on supprime les doubles
        ville.sort()
        if len(ville) == 0:
            continue
        sup = []
        mx = -1
        for v in ville:
            if v == mx:
                sup.append(v)
            mx = v
        for s in sup:
            ville.remove(s)

        nb_change = 0
        for v in ville:
            b = retournement_essai(chemin, i, v, distance=distance)
            if b:
                nb_change += 1
                continue
            b = retournement_essai(chemin, im, v, distance=distance)
            if b:
                nb_change += 1
                continue

        nbtout += nb_change

    if verbose > 0:
        print(
            f"nombre de croisements {nbtout} longueur :   \t "
            f"{longueur_chemin(chemin, distance=distance):10.0f}"
        )
    return nbtout


def tsp_kruskal_algorithm(
    points: ENSEMBLE,
    size: int = 20,
    length: int = 10,
    max_iter: Optional[int] = None,
    distance: Optional[DISTANCE] = None,
    verbose: int = 0,
) -> ENSEMBLE:
    """
    Finds the shortest path going through all points,
    points require to be a 2 dimensional space.

    :param points: list 2-tuple (X,Y)
    :param size: the 2D plan is split into square zones
    :param length: sub path
    :param max_iter: max number of iterations
    :param distance: distance function
    :return: path

    The distance is a function which takes two tuples and returns a distance::

        def distance(p1, p2):
            # ...
            return d

    Les points identiques sont enlevés puis ajoutés à la fin.
    """
    # verification
    if distance is None:
        distance = distance_euclidian
    unique = set()
    for point in points:
        if isinstance(point, list):
            raise TypeError("points cannot be list")
        unique.add(point)

    # remove duplicates
    groups = {}
    for p in points:
        x, y = p[:2]
        if (x, y) in groups:
            groups[x, y].append(p)
        else:
            groups[x, y] = [p]

    before = len(points)
    points = [v[0] for v in groups.values()]

    if verbose > 0:
        print(f"[tsp_kruskal_algorithm] with no duplicates {len(points)} <= {before}")

    # begin of the algortihm
    if verbose > 0:
        print(f"[tsp_kruskal_algorithm] arbre_poids_minimal nb={len(points)}")
    di = arbre_poids_minimal(points, size, distance=distance)
    arbre = di["arbre"]
    X, Y = di["X"], di["Y"]

    if verbose > 0:
        print(f"[tsp_kruskal_algorithm] circuit_eulerien X={X} Y={Y}")
    chemin = circuit_eulerien(points, arbre, verbose=verbose)

    if len(chemin) != len(points):
        raise RuntimeError(
            "The path should include all points: path:{0} points:{1}".format(
                len(chemin), len(points)
            )
        )

    if verbose > 0:
        print("[tsp_kruskal_algorithm] circuit_hamiltonien")

    neurone = circuit_hamiltonien(chemin)
    neurones = [points[i] for i in neurone]

    if verbose > 0:
        print("[tsp_kruskal_algorithm] amelioration_chemin")

    amelioration_chemin(
        neurones,
        size,
        X,
        Y,
        length,
        max_iter=max_iter,
        distance=distance,
        verbose=verbose,
    )

    # we add duplicates back
    final = []
    for p in neurones:
        x, y = p[:2]
        g = groups[x, y]
        if len(g) == 1:
            final.append(p)
        else:
            final.extend(g)
    return final


def circuit_eulerien(
    villes: ENSEMBLE, arbre: List[List[int]], verbose: int = 0
) -> List[int]:
    """
    Définit un circuit eulérien, villes contient la liste des villes,
    tandis que arbre est une liste de listes, ``arbre[i]`` est la liste des villes
    connectées à la ville *i*,
    on suppose que arbre est un graphe de poids minimal non orienté,
    l'algorithme ne marche pas s'il existe des villes confondues,
    un circuit eulérien passe par tous les arêtes une et une seule fois.
    """

    # on choisit une ville qui est une extrémité et parmi celle-là on la
    # choisit au hasard
    has = []
    for i in range(0, len(villes)):
        n = len(arbre[i])
        if n == 1:
            has.append(i)

    bm = random.randint(0, len(has) - 1)
    bm = has[bm]

    # vecteur, le circuit eulérien contient
    # nécessairement 2 * len (villes) noeuds puisque c'est
    # le graphe eulérien d'un arbre de poids minimal non orienté
    vec = (1, 1)
    chemin = [bm]
    done = set()
    done.add(bm)
    iter = []
    while len(done) < len(villes):
        iter.append(len(done))
        if verbose > 1 and len(iter) % 1000 == 0:
            print(
                f"  circuit_eulerien: iter={len(iter)} len(done)={len(done)} "
                f"len(villes)={len(villes)}"
            )
            if len(done) == iter[-1000]:
                # there is apparently something wrong
                break
        v = villes[bm]
        ma = -math.pi - 1
        bvec = vec
        opvec = oppose_vecteur(vec)
        bl = None
        for k in range(0, len(arbre[bm])):
            la = arbre[bm][k]
            vec2 = vecteur_points(v, villes[la])
            if vec2 == (0.0, 0.0):
                # same point, we keep the same direction
                if la not in done:
                    bl = la
                    bvec = vec2
                    # no need to go further if the points are equal
                    break
                # we skip
                continue
            if opvec == vec2:
                angle = -math.pi
            else:
                cos = vecteur_cosinus(vec, vec2)
                sin = vecteur_sinus(vec, vec2)
                angle = math.atan2(sin, cos)
            if angle > ma:
                ma = angle
                bl = la
                bvec = vec2

        if bl is not None:
            if bl not in done:
                chemin.append(bl)
                done.add(bl)
            bm = bl
            if bvec != (0.0, 0.0):
                vec = bvec
        else:
            # something is wrong (it might an issue with duplicated points)
            rows = []
            for i, p in enumerate(villes):
                rows.append(f"p{i}: {p[0]},{p[1]}")
            for i, c in enumerate(chemin):
                rows.append(f"c{i}: i={c} -> {villes[c][0]},{villes[c][1]}")
            rows.append(f"bm={bm} ma={ma} bvec={vec2} vec={vec} bl={bl}")
            rows.append(f"arbre[{bm}]={arbre[bm]}")
            rows.append(f"arbre[{arbre[bm][0]}]={arbre[arbre[bm][0]]}")
            mes = "\n".join(rows)
            raise RuntimeError("this case should not happen\n" + mes)

    if len(done) < len(villes):
        # something is wrong (it might an issue with duplicated points)
        rows = []
        for i, p in enumerate(villes):
            rows.append(f"p{i}: {p[0]},{p[1]}")
        for i, c in enumerate(chemin):
            rows.append(f"c{i}: i={c} -> {villes[c][0]},{villes[c][1]}")
        rows.append(f"bm={bm} ma={ma} bvec={vec2} vec={vec} bl={bl}")
        mes = "\n".join(rows)
        raise RuntimeError("circuit_eulerien cannot give a path:\n" + mes)

    return chemin


def amelioration_chemin(
    chemin: ENSEMBLE,
    taille_zone: int,
    X: float,
    Y: float,
    taille: int = 10,
    max_iter: Optional[int] = None,
    distance: Optional[DISTANCE] = None,
    verbose: int = 0,
):
    """
    Amélioration du chemin par un algorithme simple,
    utilise des retournements de taille au plus *taille*,
    traite les arcs qui se croisent,
    traite les grands arcs, utilise un quadrillage de taille *window*,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur d'un côté du carré d'une zone.
    """

    # première étape rapide
    iter = 0
    nb = 1
    while nb > 0 and (max_iter is None or iter < max_iter):
        nb = retournement(chemin, taille, distance=distance, verbose=verbose)
        iter += 1

    # amélioration
    nb = 1
    while nb > 0 and (max_iter is None or iter < max_iter):
        nb = retournement(chemin, taille, distance=distance, verbose=verbose)
        nb += echange_position(
            chemin, taille // 2, taille_zone, X, Y, distance=distance, verbose=verbose
        )
        nb += supprime_croisement(
            chemin, taille_zone, X, Y, distance=distance, verbose=verbose
        )
        iter += 1


def simulation(
    points: Optional[ENSEMBLE] = None,
    size: Tuple[int, int] = (800, 500),
    zone: int = 20,
    length: int = 10,
    max_iter: Optional[int] = None,
    nb: int = 700,
    distance: Optional[DISTANCE] = None,
    verbose: int = 0,
) -> Tuple[ENSEMBLE, ENSEMBLE]:
    """
    Implémente la recherche du court chemin passant par tous
    les noeuds d'un graphe en partant d'une simplification
    avec l'algorithme de Kruskal.

    :param points: ensemble de points
    :param size: taille de l'écran
    :param zone: ...
    :param length: ...
    :param max_iter: maximum number of iteration
    :param nb: number of cities
    :param distance: distance function
    :return: see :func:`tsp_kruskal_algorithm
        <teachpyx.practice.tsp_kruskal.tsp_kruskal_algorithm>`
    """
    if points is None:
        size = x, y = size[0], size[1]
        points = construit_ville(nb, x, y)

    res = tsp_kruskal_algorithm(
        points,
        size=zone,
        length=length,
        max_iter=max_iter,
        distance=distance,
        verbose=verbose,
    )
    return points, res
