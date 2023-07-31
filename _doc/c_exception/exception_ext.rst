
.. _l-exception-ext:

=====
Usage
=====

Pile d'appel ou call stack
==========================

La `pile d'appel <https://fr.wikipedia.org/wiki/Pile_d%27ex%C3%A9cution>`_
(ou *pile d'exécution* ou *call stack*) mémorise les appels de fonctions.
La premièrel ligne est le `point d'entrée <https://fr.wikipedia.org/wiki/Point_d%27entr%C3%A9e>`_
du programme. La suivante est la seconde fonction appelée.
Si celle-ci en appelle une autre, une autre ligne est ajoutée et celle-ci
demeure jusqu'à ce qu'elle est terminée son exécution. A chaque instant,
la dernière ligne est la fonction en train de s'exécuter, les lignes précédentes
définissent le chemin que l'ordinateur a suivi pour arriver jusque là.

.. runpython::
    :showcode:

    import traceback
    import sys

    def foncA():
        print("foncA begin")
        foncB()
        print("foncA end")

    def foncB():
        print("foncB begin")
        foncC()
        print("foncB end")

    def foncC():
        print("foncC begin")
        try:
            raise Exception("erreur volontaire")
        except Exception:
            print("Erreur")
            print("\n".join(traceback.format_stack()))
        print("foncC end")

    foncA()

Récupération de la pile  d'appel
++++++++++++++++++++++++++++++++

Le module `traceback <https://docs.python.org/3/library/traceback.html>`_
permet de récupérer la pile d'appels lorsqu'une exception survient.

.. runpython::
    :showcode:
    :exception:

    def raise_exception():
        raise Exception("an error was raised")

    try:
        insidefe()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("".join(traceback.format_tb(exc_traceback)))

Il est possible de récupérer la liste des appels de fonctions
avec la fonction `extract_tb <https://docs.python.org/3/library/traceback.html#traceback.extract_tb>`_.
Cette information est précieuse pour écrire un test qui vérifie qu'une erreur
s'est bien produite à un endroit particulier, de détecter les cas particuliers comme
les boucles infinies ou d'améliorer un message d'erreur en cas de besoin
(lire `How do I write Flask's excellent debug log message to a file in production? <http://stackoverflow.com/questions/14037975/how-do-i-write-flasks-excellent-debug-log-message-to-a-file-in-production>`_).

Message d'erreur plus explicite
+++++++++++++++++++++++++++++++

Lorsqu'une erreur se produit dans une librairie de Python, le message
ne mentionne aucune information à propos du code qui l'a provoquée.

.. runpython::
    :showcode:
    :exception:

    import math
    ensemble = [1, 0, 2]
    s = 0
    for e in ensemble:
        s += math.log(e)

Typiquement dans ce cas précis, on ne sait pas quel est l'indice
de l'élément qui a provoqué l'erreur. On utilise alors un mécanisme
qui permet d'ajouter une erreur sans perdre les informations l'exception original

.. runpython::
    :showcode:
    :exception:

    import math
    ensemble = [1, 0, 2]
    s = 0
    for i, e in enumerate(ensemble):
        try:
            s += math.log(e)
        except Exception as exc:
            raise Exception("Issue with element {0}".format(i)) from exc

La dernière partie de la dernière ligne est importante :
``from exc``.  langage garde ainsi la trace de la première
exception.

Conventions
===========

Erreur ou code d'erreur
+++++++++++++++++++++++

.. todoext::
    :title: terminer la section Erreur ou code d'erreur

    parler aussi de coûts d'une exception,
    libération des ressources
