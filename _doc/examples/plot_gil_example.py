# coding: utf-8
"""
======
Le GIL
====== 

Le GIL ou `Global Interpreter Lock <https://en.wikipedia.org/wiki/Global_interpreter_lock>`_
est un verrou unique auquel l'interpréteur Python fait appel constamment 
pour protéger tous les objets qu'il manipule contre des accès concurrentiels.

Deux listes en parallel
=======================
 
On mesure le temps nécessaire pour créer deux liste et comparer ce
temps avec celui que cela prendrait en parallèle.
"""
import timeit
import time
from concurrent.futures import ThreadPoolExecutor


def create_list(n):
    res = []
    for i in range(n):
        res.append(i)
    return res


timeit.timeit("create_list(100000)", globals=globals(), number=100)

######################################
# En parallèle avec le module `concurrent.futures
# <https://docs.python.org/3/library/concurrent.futures.html>`_
# et deux appels à la même fonction.


def run2(nb):
    with ThreadPoolExecutor(max_workers=2) as executor:
        for res in executor.map(create_list, [nb, nb + 1]):
            pass


timeit.timeit("run2(100000)", globals=globals(), number=100)


######################################
# C'est plus long que si les calculs étaient lancés les uns après les autres.
# Ce temps est perdu à synchroniser les deux threads bien que les
# deux boucles n'aient rien à échanger. Chaque thread passe son
# temps à attendre que l'autre ait terminé de mettre à jour sa
# liste et le *GIL* impose que ces mises à jour aient lieu une après l'autre.
#
# Un autre scénario
# =================
#
# Au lieu de mettre à jour une liste, on va lancer un thread
# qui ne fait rien qu'attendre. Donc le *GIL* n'est pas impliqué.


def attendre(t=0.009):
    time.sleep(t)
    return None


timeit.timeit("attendre()", globals=globals(), number=100)


######################################
#


def run3(t):
    with ThreadPoolExecutor(max_workers=2) as executor:
        for res in executor.map(attendre, [t, t + 0.001]):
            pass


timeit.timeit("run3(0.009)", globals=globals(), number=100)


######################################
# Les deux attentes se font en parallèle car le temps moyen est
# significativement inférieur à la somme des deux attentes.
