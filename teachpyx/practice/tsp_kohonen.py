# coding: utf-8
import random
import math
import functools
from typing import List, Tuple, Optional

ENSEMBLE = List[Tuple[float, float]]


def construit_ville(n: int, x: int = 1000, y: int = 700) -> ENSEMBLE:
    """
    Tire aléatoirement *n* villes dans un carré ``x * y``,
    on choisit ces villes de sorte qu'elles ne soient pas trop proches.
    """
    # deux villes ne pourront pas être plus proches que mind
    mind = math.sqrt(x * x + y * y) / (n * 0.75)
    # liste vide
    lt = []
    while n > 0:
        # on tire aléatoirement les coordonnées d'une ville
        xx = x * random.random()
        yy = y * random.random()
        # on vérifie qu'elle n'est pas trop proche d'aucune autre ville
        ajout = True
        for t in lt:
            d1 = t[0] - xx
            d2 = t[1] - yy
            d = math.sqrt(d1 * d1 + d2 * d2)
            if d < mind:
                ajout = False  # ville trop proche
        # si la ville n'est pas trop proche des autres, on l'ajoute à la liste
        if ajout:
            lt.append((xx, yy))
            n -= 1  # une ville en moins à choisir
    return lt


def construit_liste_neurones(villes: ENSEMBLE, nb: int = 0) -> ENSEMBLE:
    """
    Place les neurones sur l'écran,
    il y a autant de neurones que de villes,
    le paramètre villes est la liste des villes.
    """
    if nb == 0:
        nb = len(villes)

    # coordonnées maximale
    maxx, maxy = 0, 0
    for v in villes:
        if v[0] > maxx:
            maxx = v[0]
        if v[1] > maxy:
            maxy = v[1]

    maxx /= 2
    maxy /= 2

    if nb > 1:
        # dispose les neurones en ellipse
        n = []
        for i in range(0, nb):
            x = maxx + maxx * math.cos(math.pi * 2 * float(i) / nb) / 4
            y = maxy + maxy * math.sin(math.pi * 2 * float(i) / nb) / 4
            n.append((x, y))
        return n
    n = [(maxx, maxy)]
    return n


def distance_euclidienne_carree(
    p1: Tuple[float, float], p2: Tuple[float, float]
) -> float:
    """
    Calcule la distance euclidienne entre deux points.
    """
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return x * x + y * y


def ajoute_vecteur(
    v: Tuple[float, float], n: Tuple[float, float]
) -> Tuple[float, float]:
    """
    Ajoute deux vecteurs entre eux.
    """
    return (v[0] + n[0], v[1] + n[1])


def soustrait_vecteur(
    v: Tuple[float, float], n: Tuple[float, float]
) -> Tuple[float, float]:
    """
    Soustrait deux vecteurs.
    """
    return (v[0] - n[0], v[1] - n[1])


def multiplie_vecteur(v: Tuple[float, float], f: float) -> Tuple[float, float]:
    """
    Multiplie un vecteur par un scalaire.
    """
    return (v[0] * f, v[1] * f)


def poids_attirance(p: Tuple[float, float], dist: Tuple[float, float]) -> float:
    """
    Calcule le poids d'attraction d'une neurone vers une ville.
    """
    d = p[0] * p[0] + p[1] * p[1]
    d = math.sqrt(d)
    d = dist / (d + dist)
    return d


def vecteur_norme(p: Tuple[float, float]) -> float:
    """
    Calcul la norme d'un vecteur.
    """
    return math.sqrt(p[0] * p[0] + p[1] * p[1])


def deplace_neurone(
    n: Tuple[float, float],
    villes: ENSEMBLE,
    neurones: ENSEMBLE,
    dist_w: float,
    forces: List[float],
    compte: List[int],
) -> int:
    """
    Déplace le neurone de plus proche de la ville *n*,
    déplace ses voisins.

    :param villes: liste des villes
    :param neurones: liste des neurones
    :param dist: distance d'attirance
    :param forces: force de déplacement des voisins du neurones
    :param compte: incrémente compte [n] où n est l'indice du neurone choisi
    :return: indice du neurone le plus proche
    """
    # recherche du neurone le plus proche
    v = villes[n]
    proche = 0
    dist = distance_euclidienne_carree(v, neurones[0])
    for i in range(1, len(neurones)):
        d = distance_euclidienne_carree(v, neurones[i])
        if d < dist:
            dist = d
            proche = i

    # vecteur de déplacement
    i = proche
    compte[i] += 1
    n = neurones[i]
    vec = soustrait_vecteur(v, n)
    poids = poids_attirance(vec, dist_w)
    vec = multiplie_vecteur(vec, poids)
    n = ajoute_vecteur(n, vec)
    neurones[i] = n

    # déplacement des voisins
    for k in range(0, len(forces)):
        i1 = (i + k + 1) % len(neurones)
        i2 = (i - k - 1 + len(neurones)) % len(neurones)
        n1 = neurones[i1]
        n2 = neurones[i2]

        vec = soustrait_vecteur(n, n1)
        poids = poids_attirance(vec, dist_w)
        vec = multiplie_vecteur(vec, poids)
        vec = multiplie_vecteur(vec, forces[k])
        n1 = ajoute_vecteur(n1, vec)

        vec = soustrait_vecteur(n, n2)
        poids = poids_attirance(vec, dist_w)
        vec = multiplie_vecteur(vec, poids)
        vec = multiplie_vecteur(vec, forces[k])
        n2 = ajoute_vecteur(n2, vec)

        neurones[i1] = n1
        neurones[i2] = n2

    return proche


def iteration(
    villes: ENSEMBLE,
    neurones: ENSEMBLE,
    dist: float,
    forces: List[float],
    compte_v: List[int],
    compte_n: List[int],
) -> Tuple[int, int]:
    """
    Choisit une ville aléatoirement et attire le neurones le plus proche,
    choisit cette ville parmi les villes les moins fréquemment choisies.

    :param villes: liste des villes
    :param neurones: liste des neurones
    :param dist: distance d'attirance
    :param forces: force de déplacement des voisins du neurones
    :param compte_v: incrémente compte_v [n] où n est l'indice de la ville choisie
    :param compte_n: incrémente compte_n [n] où n est l'indice du neurone choisi
    :return: indices de la ville et du neurone le plus proche
    """
    m = min(compte_v)
    ind = [i for i in range(0, len(villes)) if compte_v[i] == m]
    n = random.randint(0, len(ind) - 1)
    n = ind[n]
    compte_v[n] += 1
    return n, deplace_neurone(n, villes, neurones, dist, forces, compte_n)


def modifie_structure(neurones: ENSEMBLE, compte: List[int], nb_sel: int):
    """
    Modifie la structure des neurones, supprime les neurones jamais
    déplacés, et ajoute des neurones lorsque certains sont trop sollicités.
    """

    def cmp_add(i, j):
        return -1 if i[0] < j[0] else (1 if i[0] > j[0] else 0)

    if nb_sel > 0:
        # supprime les neurones les moins sollicités
        sup = [i for i in range(0, len(neurones)) if compte[i] == 0]
        if len(sup) > 0:
            sup.sort()
            sup.reverse()
            for i in sup:
                del compte[i]
                del neurones[i]

        # on ajoute un neurone lorsque max (compte) >= 2 * min (compte)
        add = []
        for i in range(0, len(compte)):
            if compte[i] > nb_sel:
                d1 = math.sqrt(
                    distance_euclidienne_carree(
                        neurones[i], neurones[(i + 1) % len(neurones)]
                    )
                )
                d2 = math.sqrt(
                    distance_euclidienne_carree(
                        neurones[i], neurones[(i - 1 + len(neurones)) % len(neurones)]
                    )
                )
                if d1 > d2:
                    d1 = d2
                p = neurones[i]
                p = (
                    p[0] + random.randint(0, int(d1 / 2)),
                    p[1] + random.randint(0, int(d1 / 2)),
                )
                add.append((i, p, 0))

        add = list(sorted(add, key=functools.cmp_to_key(cmp_add)))
        add.reverse()
        for a in add:
            neurones.insert(a[0], a[1])
            compte.insert(a[0], a[2])

    # on remet les compteurs à zéros
    for i in range(0, len(compte)):
        compte[i] = 0


def moyenne_proximite(villes: ENSEMBLE) -> float:
    """
    Retourne la distance moyenne entre deux villes les plus proches.
    """
    c = 0
    m = 0
    for v in villes:
        mn = 100000000
        for vv in villes:
            if v == vv:
                continue
            d = distance_euclidienne_carree(v, vv)
            if d < mn:
                mn = d
        c += 1
        m += math.sqrt(mn)
    m /= float(c)
    return m


def distance_chemin(p: ENSEMBLE) -> float:
    """
    Calcule la distance du chemin.
    """
    d = 0
    for i in range(0, len(p)):
        d += ((p[i][0] - p[i - 1][0]) ** 2 + (p[i][1] - p[i - 1][1]) ** 2) ** 0.5
    return d


def simulation(
    villes: Optional[ENSEMBLE] = None,
    size: Tuple[int, int] = (800, 500),
    nb: int = 200,
    tour: int = 2,
    dist_ratio: float = 4,
    fs: Tuple[float, float, float, float, float] = (1.5, 1, 0.75, 0.5, 0.25),
    max_iter: int = 12000,
    alpha: float = 0.99,
    beta: float = 0.90,
    verbose: int = 0,
) -> Tuple[ENSEMBLE, ENSEMBLE]:
    """
    :param villes: ensemble de villes ou tirage aléatoire si non défini.
    :param size: taille de l'écran
    :param fs: paramètres
    :param max_iter: nombre d'itérations maximum
    :param alpha: paramètre alpha
    :param beta: paramètre beta
    :param dist_ratio: ratio distance
    :param tour: nombre de tours
    :param nb: nombre de points
    :return: list des neurones

    .. note:: solution

        La liste des neurones n'est pas encore la solution,
        il faut apparier les villes
        à ces neurones pour déterminer plus court chemin.
    """
    if villes is None:
        size = x, y = size[0], size[1]
        villes = construit_ville(nb, x, y)

    neurones = construit_liste_neurones(villes, 3)
    compte_n = [0 for i in neurones]
    compte_v = [0 for i in villes]
    maj = tour * len(villes)
    dist = moyenne_proximite(villes) * dist_ratio

    iter = 0
    while iter < max_iter:
        iter += 1

        distance = distance_chemin(neurones) if len(neurones) >= len(villes) else None
        if verbose > 0 and iter % len(villes) * 10 == 0:
            print(
                f"[simulation] {iter}/{max_iter}, "
                f"neurones={len(neurones)}/{len(villes)}, "
                f"distance={distance}, fs={fs}"
            )

        if iter % maj == 0:
            modifie_structure(neurones, compte_n, tour)
            dist *= alpha
            f2 = tuple(w * beta for w in fs)
            fs = f2

        iteration(villes, neurones, dist, fs, compte_v, compte_n)

    if verbose > 0:
        print(
            f"[simulation] end {iter} "
            f"neurones={len(neurones)}/{len(villes)}, "
            f"distance={distance}, fs={fs}"
        )
    return villes, neurones
