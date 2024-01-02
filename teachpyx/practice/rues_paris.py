# coding: utf-8
from typing import Callable, Dict, List, Optional, Tuple
import random
import math
from ..tools.data_helper import download_and_unzip


def distance_paris(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """
    Distance euclidienne approchant la distance de Haversine
    (uniquement pour Paris).
    """
    return ((lat1 - lat2) ** 2 + (lng1 - lng2) ** 2) ** 0.5 * 90


def distance_haversine(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """
    Calcule la distance de Haversine
    `Haversine formula <http://en.wikipedia.org/wiki/Haversine_formula>`_
    """
    radius = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lng2 - lng1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
        math.radians(lat1)
    ) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d


def get_data(
    url: str = "https://github.com/sdpython/teachpyx/raw/main/_data/paris_54000.zip",
    dest: str = ".",
    timeout: int = 10,
    verbose: bool = False,
    keep: int = -1,
) -> List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]]:
    """
    Retourne les données des rues de Paris. On suppose que les arcs sont uniques
    et qu'il si :math:`j \\rightarrow k` est présent,
    :math:`j \\rightarrow k` ne l'est pas.
    Ceci est vérifié par un test.

    :param url: location of the data
    :param dest: répertoire dans lequel télécharger les données
    :param timeout: timeout (seconds) when estabishing the connection
    :param verbose: affiche le progrès
    :param keep: garde tout si la valeur est -1,
        sinon garde les 1000 premières rues, ces rues sont choisies
        de façon à construire un ensemble connexe
    :return: liste d'arcs

    Un arc est défini par un 6-uple contenant les informations suivantes :

    - v1: indice du premier noeud
    - v2: indice du second noeud
    - ways: sens unique ou deux sens
    - p1: coordonnées du noeud 1
    - p2: coordonnées du noeud 2
    - d: distance
    """
    data = download_and_unzip(url=url, timeout=timeout, verbose=verbose)
    name = data[0]
    with open(name, "r") as f:
        lines = f.readlines()

    vertices = []
    edges = []
    for i, line in enumerate(lines):
        spl = line.strip("\n\r").split(" ")
        if len(spl) == 2:
            vertices.append((float(spl[0]), float(spl[1])))
        elif len(spl) == 5 and i > 0:
            v1, v2 = int(spl[0]), int(spl[1])
            ways = int(spl[2])  # dans les deux sens ou pas
            p1 = vertices[v1]
            p2 = vertices[v2]
            edges.append(
                (v1, v2, ways, p1, p2, distance_haversine(p1[0], p1[1], p2[0], p2[1]))
            )
        elif i > 0:
            raise RuntimeError(f"Unable to interpret line {i}: {line!r}")

    pairs = {}
    for e in edges:
        p = e[:2]
        if p in pairs:
            raise ValueError(f"Unexpected pairs, already present: {e}")
        pairs[p] = True

    if keep is not None:
        new_vertices = {}
        already_added = set()
        new_edges = []
        for _ in range(0, int(keep**0.5) + 1):
            for edge in edges:
                if edge[:2] in already_added:
                    continue
                p1, p2 = edge[-3:-1]
                if (
                    len(new_vertices) > 0
                    and p1 not in new_vertices
                    and p2 not in new_vertices
                ):
                    # On considère des rues connectées à des rues déjà sélectionnées.
                    continue
                if p1 not in new_vertices:
                    new_vertices[p1] = len(new_vertices)
                if p2 not in new_vertices:
                    new_vertices[p2] = len(new_vertices)
                i1, i2 = new_vertices[p1], new_vertices[p2]
                new_edges.append((i1, i2, edge[2], p1, p2, edge[-1]))
                already_added.add(edge[:2])
                if len(new_edges) >= keep:
                    break
            if len(new_edges) >= keep:
                break
        items = [(v, i) for i, v in new_vertices.items()]
        items.sort()
        vertices = [_[1] for _ in items]
        edges = new_edges

    return edges, vertices


def graph_degree(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]]
) -> Dict[Tuple[int, int], int]:
    """
    Calcul le degré de chaque noeud.

    :param edges: list des arcs
    :return: degrés
    """
    nb_edges = {}
    for edge in edges:
        v1, v2 = edge[:2]
        nb_edges[v1] = nb_edges.get(v1, 0) + 1
        nb_edges[v2] = nb_edges.get(v2, 0) + 1
    return nb_edges


def possible_edges(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]],
    threshold: float,
    distance: Callable = distance_haversine,
):
    """
    Construit la liste de tous les arcs possibles en
    filtrant sur la distance à vol d'oiseau.

    :param edges: list des arcs
    :param threshold: seuil au-delà duquel deux noeuds ne seront pas connectés
    :param distance: la distance de Haversine est beaucoup trop
        longue sur de grands graphes, on peut la changer
    :return: arcs possibles (symétrique --> incluant edges)
    """
    vertices: Dict[int : Tuple[float, float]] = {e[0]: e[3] for e in edges}
    vertices.update({e[1]: e[4] for e in edges})

    possibles = {(e[0], e[1]): e[-1] for e in edges}
    possibles.update({(e[1], e[0]): e[-1] for e in edges})
    # initial = possibles.copy()
    for i1, v1 in vertices.items():
        for i2, v2 in vertices.items():
            if i1 >= i2:
                continue
            d = distance(*(v1 + v2))
            if d < threshold:
                possibles[i1, i2] = d
                possibles[i2, i1] = d

    return possibles


def bellman(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]],
    max_iter: int = 20,
    allow: Optional[Callable] = None,
    init: Optional[Dict[Tuple[int, int], float]] = None,
    verbose: bool = False,
) -> Dict[Tuple[int, int], float]:
    """
    Implémente l'algorithme de `Bellman-Ford <http://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>`_.

    :param edges: liste de tuples (noeud 1, noeud 2, ?, ?, ?, poids)
    :param max_iter: nombre d'itérations maximal
    :param allow: fonction déterminant si l'algorithme
        doit envisager cette liaison ou pas
    :param init: initialisation (pour pouvoir continuer après une première exécution)
    :param verbose: afficher le progrès
    :return: listes des arcs et des distances calculées
    """

    if init is None:
        init: Dict[Tuple[int, int], float] = {(e[0], e[1]): e[-1] for e in edges}
        init.update({(e[1], e[0]): e[-1] for e in edges})

    def always_true(e):
        return True

    if allow is None:
        allow = always_true

    edges_from = {}
    for e in edges:
        if e[0] not in edges_from:
            edges_from[e[0]] = []
        if e[1] not in edges_from:
            edges_from[e[1]] = []
        edges_from[e[0]].append(e)
        if len(e) == 2:
            edges_from[e[1]].append((e[1], e[0], 1.0))
        elif len(e) == 3:
            edges_from[e[1]].append((e[1], e[0], e[2]))
        elif len(e) == 6:
            edges_from[e[1]].append((e[1], e[0], e[2], e[4], e[3], e[5]))
        else:
            raise ValueError(
                f"an edge should be a tuple of 2, 3, or 6 elements, "
                f"last item is the weight, not:\n{e}"
            )

    modif = 1
    total_possible_edges = (len(edges_from) ** 2 - len(edges_from)) // 2
    it = 0
    while modif > 0:
        modif = 0
        # to avoid RuntimeError: dictionary changed size during iteration
        initc = init.copy()
        s = 0
        for i, d in initc.items():
            if allow(i):
                fromi2 = edges_from[i[1]]
                s += d
                for e in fromi2:
                    # on fait attention à ne pas ajouter de boucle sur le même
                    # noeud
                    if i[0] == e[1]:
                        continue
                    new_e = i[0], e[1]
                    new_d = d + e[-1]
                    if new_e not in init or init[new_e] > new_d:
                        init[new_e] = new_d
                        modif += 1
        if verbose:
            print(
                f"iteration {it} #modif {modif} # "
                f"{len(initc) // 2}/{total_possible_edges} = "
                f"{len(initc) * 50 / total_possible_edges:1.2f}%"
            )
        it += 1
        if it > max_iter:
            break

    return init


def kruskal(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]],
    extension: Dict[Tuple[int, int], float],
) -> List[Tuple[int, int]]:
    """
    Applique l'algorithme de Kruskal (ou ressemblant) pour choisir les arcs à ajouter.

    :param edges: listes des arcs
    :param extension: résultat de l'algorithme de Bellman
    :return: added_edges
    """

    original: Dict[Tuple[int, int], float] = {(e[0], e[1]): e[-1] for e in edges}
    original.update({(e[1], e[0]): e[-1] for e in edges})
    additions: Dict[Tuple[int, int], float] = {
        k: v for k, v in extension.items() if k not in original
    }
    additions.update({(k[1], k[0]): v for k, v in additions.items()})

    degre: Dict[Tuple[int, int], int] = {}
    for k, v in original.items():  # original est symétrique
        degre[k[0]] = degre.get(k[0], 0) + 1

    tri = [
        (v, k)
        for k, v in additions.items()
        if degre[k[0]] % 2 == 1 and degre[k[1]] % 2 == 1
    ]
    tri.extend(
        [
            (v, k)
            for k, v in original.items()
            if degre[k[0]] % 2 == 1 and degre[k[1]] % 2 == 1
        ]
    )
    tri.sort()

    impairs = sum(v % 2 for k, v in degre.items())
    added_edges = []
    if impairs > 2:
        for v, a in tri:
            if degre[a[0]] % 2 == 1 and degre[a[1]] % 2 == 1:
                # il faut refaire le test car degre peut changer à chaque
                # itération
                degre[a[0]] += 1
                degre[a[1]] += 1
                added_edges.append(a + (v,))
                impairs -= 2
                if impairs <= 0:
                    break
    return added_edges


def eulerien_extension(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]],
    max_iter: int = 20,
    alpha: float = 0.5,
    distance: Callable = distance_haversine,
    verbose: bool = False,
) -> List[Tuple[int, int]]:
    """
    Construit une extension eulérienne d'un graphe.

    :param edges: liste des arcs
    :param max_iter: nombre d'itérations pour la fonction @see fn bellman
    :param alpha: coefficient multiplicatif de ``max_segment``
    :param distance: la distance de Haversine est beaucoup trop
        longue sur de grands graphes, on peut la changer
    :param verbose: afficher l'avancement
    :return: added edges
    """
    max_segment = max(e[-1] for e in edges)

    possibles = possible_edges(edges, max_segment * alpha, distance=distance)

    init = bellman(edges, allow=lambda e: e in possibles)
    added = kruskal(edges, init)
    d = graph_degree(edges + added)
    allow = [k for k, v in d.items() if v % 2 == 1]
    totali = 0
    while len(allow) > 0:
        if verbose:
            print(f"------- # odd vertices {len(allow)} iteration {totali}")
        allowset = set(allow)
        init = bellman(
            edges,
            max_iter=max_iter,
            allow=lambda e: e in possibles or e[0] in allowset or e[1] in allowset,
            init=init,
            verbose=verbose,
        )
        added = kruskal(edges, init)
        d = graph_degree(edges + added)
        allow = [k for k, v in d.items() if v % 2 == 1]
        totali += 1
        if totali > 20:
            # tant pis, ça ne marche pas
            break

    return added


def connected_components(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]]
) -> Dict[int, int]:
    """
    Computes the connected components.

    :param edges: edges
    :return: dictionary { vertex : id of connected components }
    """
    res = {}
    for k in edges:
        for _ in k[:2]:
            if _ not in res:
                res[_] = _
    modif = 1
    while modif > 0:
        modif = 0
        for k in edges:
            a, b = k[:2]
            r, s = res[a], res[b]
            if r != s:
                m = min(res[a], res[b])
                res[a] = res[b] = m
                modif += 1

    return res


def euler_path(
    edges: List[Tuple[int, int, int, Tuple[float, float], Tuple[float, float], float]],
    added_edges,
):
    """
    Computes an eulerian path. We assume every vertex has an even degree.

    :param edges: initial edges
    :param added_edges: added edges
    :return: path, list of `(vertex, edge)`
    """
    alledges = {}
    edges_from = {}
    somme = 0.0
    for e in edges:
        k = e[:2]  # indices des noeuds
        v = e[-1]  # distance
        alledges[k] = ["street", *k, v]
        a, b = k
        alledges[b, a] = alledges[a, b]
        if a not in edges_from:
            edges_from[a] = []
        if b not in edges_from:
            edges_from[b] = []
        edges_from[a].append(alledges[a, b])
        edges_from[b].append(alledges[a, b])
        somme += v

    for e in added_edges:  # il ne faut pas enlever les doublons
        k = e[:2]  # indices ds noeuds
        v = e[-1]  # distance
        a, b = k
        alledges[k] = ["jump", *k, v]
        alledges[b, a] = alledges[a, b]
        if a not in edges_from:
            edges_from[a] = []
        if b not in edges_from:
            edges_from[b] = []
        edges_from[a].append(alledges[a, b])
        edges_from[b].append(alledges[a, b])
        somme += v

    # les noeuds de degré impair
    odd = [a for a, v in edges_from.items() if len(v) % 2 == 1]
    if len(odd) > 0:
        raise ValueError("Some vertices have an odd degree.")
    # les noeuds de degré 2, on les traverse qu'une fois
    two = [a for a, v in edges_from.items() if len(v) == 2]
    begin = two[0]

    # checking
    for v, le in edges_from.items():
        # v est une extrémité
        for e in le:
            # to est l'autre extrémité
            to = e[1] if v != e[1] else e[2]
            if to not in edges_from:
                raise RuntimeError(f"Unable to find vertex {to} for edge {to},{v}")
            if to == v:
                raise RuntimeError(f"Circular edge {to}")

    # On sait qu'il existe un chemin. La fonction explore les arcs
    # jusqu'à revenir à son point de départ. Elle supprime les arcs
    # utilisées de edges_from.
    path = _explore_path(edges_from, begin)

    # Il faut s'assurer que le chemin ne contient pas de boucles non visitées.
    while len(edges_from) > 0:
        # Il reste des arcs non visités. On cherche le premier
        # arc connecté au chemin existant.
        start = None
        for i, p in enumerate(path):
            if p[0] in edges_from:
                start = i, p
                break
        if start is None:
            raise RuntimeError(
                f"start should not be None\npath={path}\nedges_from={edges_from}"
            )
        sub = _explore_path(edges_from, start[1][0])
        i = start[0]
        path[i : i + 1] = path[i : i + 1] + sub
    return path


def _delete_edge(edges_from, n: int, to: int):
    """
    Removes an edge from the graph.

    :param edges_from: structure which contains the edges (will be modified)
    :param n: first vertex
    :param to: second vertex
    :return: the edge
    """
    le = edges_from[to]
    f = None
    for i, e in enumerate(le):
        if (e[1] == to and e[2] == n) or (e[2] == to and e[1] == n):
            f = i
            break

    assert f is not None
    del le[f]
    if len(le) == 0:
        del edges_from[to]

    le = edges_from[n]
    f = None
    for i, e in enumerate(le):
        if (e[1] == to and e[2] == n) or (e[2] == to and e[1] == n):
            f = i
            break

    assert f is not None
    keep = le[f]
    del le[f]
    if len(le) == 0:
        del edges_from[n]

    return keep


def _explore_path(edges_from, begin):
    """
    Explores an eulerian path, remove used edges from edges_from.

    :param edges_from: structure which contains the edges (will be modified)
    :param begin: first vertex to use
    :return: path
    """
    path = [(begin, None)]
    stay = True
    while stay and len(edges_from) > 0:
        n = path[-1][0]
        if n not in edges_from:
            # fin
            break
        le = edges_from[n]

        if len(le) == 1:
            h = 0
            e = le[h]
            to = e[1] if n != e[1] else e[2]
        else:
            to = None
            nb = 100
            while to is None or to == begin:
                h = random.randint(0, len(le) - 1) if len(le) > 1 else 0
                e = le[h]
                to = e[1] if n != e[1] else e[2]
                nb -= 1
                if nb < 0:
                    raise RuntimeError(f"algorithm issue {len(path)}")

        if len(edges_from[to]) == 1:
            if begin != to:
                raise RuntimeError("wrong algorithm")
            else:
                stay = False

        keep = _delete_edge(edges_from, n, to)
        path.append((to, keep))

    return path[1:]
