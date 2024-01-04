import os
from ..practice.tsp_kohonen import (
    ENSEMBLE,
    iteration,
    modifie_structure,
    moyenne_proximite,
    construit_ville,
    construit_liste_neurones,
)
from ..tools.display.pygame_helper import wait_event, empty_main_loop


def display_neurone(neurones: ENSEMBLE, screen, bn: int, pygame):
    """
    Dessine les neurones à l'écran.
    """
    color = 0, 0, 255
    color2 = 0, 255, 0
    for n in neurones:
        pygame.draw.circle(screen, color, (int(n[0]), int(n[1])), 5)
    v = neurones[bn]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 5)
    if len(neurones) > 1:
        pygame.draw.lines(screen, color, True, neurones, 2)


def display_ville(villes: ENSEMBLE, screen, bv: int, pygame):
    """
    Dessine les villes à l'écran.
    """
    color = 255, 0, 0
    color2 = 0, 255, 0
    for v in villes:
        pygame.draw.circle(screen, color, (int(v[0]), int(v[1])), 5)
    v = villes[bv]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 5)


def pygame_simulation(
    pygame,
    folder=None,
    size=(800, 500),
    nb=200,
    tour=2,
    dist_ratio=4,
    fs=(1.5, 1, 0.75, 0.5, 0.25),
    max_iter=12000,
    alpha=0.99,
    beta=0.90,
    first_click=False,
    flags=0,
):
    """
    See :func:`teachpyx.practice.tsp_kohonen.simulation`.

    :param pygame: module pygame
    :param first_click: attend la pression d'un clic de souris avant de commencer
    :param folder: répertoire où stocker les images de la simulation
    :param size: taille de l'écran
    :param delay: delay between two tries
    :param flags: see `pygame.display.set_mode <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    :param fs: paramètres
    :param max_iter: nombre d'itérations maximum
    :param alpha: paramètre alpha
    :param beta: paramètre beta
    :param dist_ratio: ratio distance
    :param tour: nombre de tours
    :param nb: nombre de points

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="125">
        <source
        src="https://github.com/sdpython/teachdata/raw/main/video/tsp_kohonen.mp4"
        type="video/mp4" />
        </video>

    Pour lancer la simulation::

        from teachpyx.video.tsp_kohonen_pygame import pygame_simulation
        import pygame
        pygame_simulation(pygame)
    """
    pygame.init()
    size = x, y = size[0], size[1]
    white = 255, 255, 255
    screen = pygame.display.set_mode(size, flags)
    villes = construit_ville(nb, x, y)
    neurones = construit_liste_neurones(villes, 3)
    compte_n = [0 for i in neurones]
    compte_v = [0 for i in villes]
    maj = tour * len(villes)
    dist = moyenne_proximite(villes) * dist_ratio

    if first_click:
        wait_event(pygame)
    images = [] if folder is not None else None

    iter = 0
    while iter < max_iter:
        iter += 1

        if iter % 1000 == 0:
            print("iter", iter)

        if iter % maj == 0:
            modifie_structure(neurones, compte_n, tour)
            dist *= alpha
            f2 = tuple(w * beta for w in fs)
            fs = f2

        bv, bn = iteration(villes, neurones, dist, fs, compte_v, compte_n)

        screen.fill(white)
        display_ville(villes, screen, bv, pygame)
        display_neurone(neurones, screen, bn, pygame)
        empty_main_loop(pygame)
        pygame.display.flip()

        if images is not None and iter % 10 == 0:
            images.append(screen.copy())

    if first_click:
        wait_event(pygame)

    if folder is not None:
        print("saving images")
        for it, screen in enumerate(images):
            if it % 10 == 0:
                print("saving image:", it, "/", len(images))
            image = os.path.join(folder, "image_%04d.png" % it)
            pygame.image.save(screen, image)
