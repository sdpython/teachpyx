import os
import math
import random
from typing import List, Optional, Tuple
from ..practice.tsp_kruskal import (
    ENSEMBLE,
    DISTANCE,
    arbre_poids_minimal,
    circuit_hamiltonien,
    construit_ville,
    distance_euclidian,
    echange_position,
    oppose_vecteur,
    vecteur_cosinus,
    vecteur_sinus,
    vecteur_points,
    retournement,
    supprime_croisement,
)
from ..tools.display.pygame_helper import wait_event, empty_main_loop


def tsp_kruskal_algorithm(
    points: ENSEMBLE,
    size: int = 20,
    length: int = 10,
    max_iter: Optional[int] = None,
    pygame=None,
    screen=None,
    images=None,
    distance: Optional[DISTANCE] = None,
    verbose: int = 0,
):
    """
    Finds the shortest path going through all points,
    points require to be a 2 dimensional space.

    :param points: list 2-tuple (X,Y)
    :param size: the 2D plan is split into square zones
    :param length: sub path
    :param max_iter: max number of iterations
    :param pygame: pygame for simulation
    :param screen: with pygame
    :param images: save intermediate images
    :param distance: distance function
    :param verbose: veerbosity
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
    if screen is not None:
        display_arbre(points, arbre, screen=screen, pygame=pygame)
        pygame.display.flip()
        if images is not None:
            c = screen.copy()
            for i in range(0, 5):
                images.append(c)
    if verbose > 0:
        print(f"[tsp_kruskal_algorithm] circuit_eulerien X={X} Y={Y}")
    chemin = circuit_eulerien(points, arbre, screen, pygame, verbose=verbose)

    if len(chemin) != len(points):
        raise RuntimeError(
            f"The path should include all points: "
            f"path:{len(chemin)} points:{len(points)}"
        )

    if screen is not None:
        display_chemin([points[c] for c in chemin], 0, screen=screen, pygame=pygame)
        pygame.display.flip()
        if images is not None:
            c = screen.copy()
            for i in range(0, 5):
                images.append(c)

    if verbose > 0:
        print("[tsp_kruskal_algorithm] circuit_hamiltonien")
    neurone = circuit_hamiltonien(chemin)
    neurones = [points[i] for i in neurone]
    if screen is not None:
        display_chemin(neurones, 0, screen=screen, pygame=pygame)
    if verbose > 0:
        print("[tsp_kruskal_algorithm] amelioration_chemin")

    amelioration_chemin(
        neurones,
        size,
        X,
        Y,
        length,
        screen,
        pygame=pygame,
        max_iter=max_iter,
        images=images,
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


def display_ville(villes, screen, bv, pygame):
    """
    Dessine les villes à l'écran.
    """
    color = 255, 0, 0
    color2 = 0, 255, 0
    for v in villes:
        pygame.draw.circle(screen, color, (int(v[0]), int(v[1])), 3)
    v = villes[bv]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 3)


def display_chemin(neurones, bn, screen, pygame):
    """
    Dessine le chemin à l'écran.
    """
    color = 0, 0, 255
    color2 = 0, 255, 0
    for n in neurones:
        pygame.draw.circle(screen, color, (int(n[0]), int(n[1])), 3)
    v = neurones[bn]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 3)
    if len(neurones) > 1:
        pygame.draw.lines(screen, color, True, neurones, 2)


def display_arbre(villes, arbre, mult=1, screen=None, pygame=None):
    """
    Dessine le graphe de poids minimal dꧩni par arbre.
    """
    if mult == 2:
        color = 0, 255, 0
        li = 4
    else:
        li = 1
        color = 0, 0, 255

    for i in range(0, len(villes)):
        for j in arbre[i]:
            v = (villes[i][0] * mult, villes[i][1] * mult)
            vv = (villes[j][0] * mult, villes[j][1] * mult)
            pygame.draw.line(screen, color, v, vv, li)


def circuit_eulerien(
    villes: ENSEMBLE, arbre: List[List[int]], screen, pygame, verbose: int
):
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
                f"  circuit_eulerien: iter={len(iter)} "
                f"len(done)={len(done)} len(villes)={len(villes)}"
            )
        if len(iter) > 1000 and len(done) == iter[-1000]:
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
    taille_zone: float,
    X: float,
    Y: float,
    taille: int = 10,
    screen=None,
    pygame=None,
    max_iter: Optional[int] = None,
    images=None,
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

    white = 255, 255, 255

    if pygame is not None and images is not None:
        images.append(screen.copy())

    # première étape rapide
    iter = 0
    nb = 1
    while nb > 0 and (max_iter is None or iter < max_iter):
        nb = retournement(chemin, taille, distance=distance, verbose=verbose)
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        iter += 1

    # amélioration
    nb = 1
    while nb > 0 and (max_iter is None or iter < max_iter):
        nb = retournement(chemin, taille, distance=distance, verbose=verbose)
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen=screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        nb += echange_position(
            chemin, taille // 2, taille_zone, X, Y, distance=distance, verbose=verbose
        )
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen=screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        nb += supprime_croisement(
            chemin, taille_zone, X, Y, distance=distance, verbose=verbose
        )
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen=screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        iter += 1


def pygame_simulation(
    size: Tuple[int, int] = (800, 500),
    zone: int = 20,
    length: int = 10,
    max_iter: Optional[int] = None,
    nb: int = 700,
    pygame=None,
    folder=None,
    first_click: bool = False,
    distance=None,
    flags=0,
    verbose: int = 0,
):
    """
    :param pygame: module pygame
    :param nb: number of cities
    :param first_click: attend la pression d'un clic
        de souris avant de commencer
    :param folder: répertoire où stocker les images de la simulation
    :param size: taille de l'écran
    :param delay: delay between two tries
    :param folder: folder where to save images
    :param distance: distance function
    :param flags: see `pygame.display.set_mode
        <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    :param verbose: verbosity
    :return: see :func:`tsp_kruskal_algorithm
        <teachpyx.practice.tsp_kruskal.tsp_kruskal_algorithm>`

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="250">
        <source
        src="https://github.com/sdpython/teachdata/raw/main/video/tsp_kruskal.mp4"
        type="video/mp4" />
        </video>

    Pour lancer la simulation::

        import pygame
        from teachpyx.video.tsp_kruskal_pygame import pygame_simulation
        pygame_simulation(pygame)

    Voir :ref:`l-tsp_kruskal`.
    """
    pygame.init()
    size = x, y = size[0], size[1]
    white = 255, 255, 255
    screen = pygame.display.set_mode(size, flags)
    screen.fill(white)
    points = construit_ville(nb, x, y)

    if first_click:
        wait_event(pygame)

    images = [] if folder is not None else None
    tsp_kruskal_algorithm(
        points,
        size=zone,
        length=length,
        max_iter=max_iter,
        pygame=pygame,
        screen=screen,
        images=images,
        distance=distance,
        verbose=verbose,
    )
    if verbose > 0:
        print(f"folder {folder!r}")
        print(f"images {len(images)}")

    if first_click:
        wait_event(pygame)

    if folder is not None:
        if verbose > 0:
            print("saving images")
        for it, screen in enumerate(images):
            if verbose > 0 and it % 10 == 0:
                print(f"saving image: {it}/{len(images)}")
            image = os.path.join(folder, "image_%04d.png" % it)
            pygame.image.save(screen, image)
