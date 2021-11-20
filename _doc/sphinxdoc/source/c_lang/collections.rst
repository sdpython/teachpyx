
.. _l-collections:

========================
Constructions classiques
========================

Le module :mod:`collections` propose d'autres types d'objets
qui en contiennent d'autres. Ils sont très proches des types
standards liste ou dictionnaires mais sont optimisés pour un usage
en particulier. Cela les rend plus efficaces pour celui-ci et
souvent plus lent pour les autres. Ce chapitre en recense les
plus utilisés.

.. contents::
    :local:

OrderedDict
===========

:class:`collections.OrderedDict` est un dictionnaire qui conservent
l'ordre dans lequel les éléments y ont été insérés.
Cette distinction était effective jusqu'à Python 3.7 mais
depuis cette version, le type standard `dict` conserve
également l'ordre d'insertion comme le montre l'exemple suivant.

.. runpython::
    :showcode:

    import random
    from collections import OrderedDict

    rnd = [random.randint(0, 10) for i in range(10)]

    dico = {}
    for i, h in enumerate(rnd):
        dico[h] = i
    print(list(dico))
    print(list(dico.items()))

    dico = OrderedDict()
    for i, h in enumerate(rnd):
        dico[h] = i
    print(list(dico))
    print(list(dico.items()))

Néanmoins, cette distinctions est importante à connaître pour des
langages plus bas niveau comme le C++.

namedtuple
==========

:func:`collections.namedtuple` est un tuple, donc immuable,
mais chaque élément est associé un nom.
La fonction :func:`collections.namedtuple` retourne une classe
et non une instance de classe.

.. runpython::
    :showcode:

    from collections import namedtuple

    ClassePersonne = namedtuple('Personne', ['nom', 'prenom'])

    p = ClassePersonne('George', 'Boole')
    print(p)
    print(p.nom, p.prenom)
    print(p[0], p[1])

    try:
        p.nom = "A"
    except AttributeError as e:
        print(e)

On accède à chaque élément avec un nom ou un indice.
Et on peut récupérer la liste des attributs de la classe.

.. runpython::
    :showcode:

    from collections import namedtuple

    ClassePersonne = namedtuple('Personne', ['nom', 'prenom'])
    print(ClassePersonne._fields)

Ce type de construction ne change pas un programme mais elle
le rend plus lisible.

Counter
=======

:class:`collection.Counter` est un dictionnaire spécifique dans les valeurs
sont entières. Il est très pratique pour compter les éléments.
L'exemple :ref:`comptage <l-ex-comptage>` s'écrit en une ligne.

.. runpython::
    :showcode:

    from collections import Counter

    ensemble = ['A', 'B', 'A', 'AA', 'C']
    c = Counter(ensemble)
    print(c)

deque
=====

:class:`collection.deque` est une liste qui supporte l'insertion
d'éléments en bout de liste et au début également
(`liste chaînée <https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_).

.. runpython::
    :showcode:

    from collections import deque

    ens = deque(['A', 'B'])
    ens.append('C')
    ens.appendleft('D')
    print(ens)

Il faut retenir que ce qu'on gagne en agilité se perd souvent
en performance ou en espace mémoire.
La différence n'est pas flagrante. Encore une fois,
le langage Python est lent et rend ces différences parfois négligeables.
Ces différences sont souvent significatives pour des langages
plus bas niveau.

.. runpython::
    :showcode:

    import sys
    from collections import deque
    import timeit

    def append_time_list():
        ens = list()
        for i in range(0, 10000):
            ens.append(i)
        return ens

    def append_time_deque():
        ens = deque()
        for i in range(0, 10000):
            ens.append(i)
        return ens

    print('list', timeit.timeit(append_time_list, number=100))
    print('deque', timeit.timeit(append_time_deque, number=100))
