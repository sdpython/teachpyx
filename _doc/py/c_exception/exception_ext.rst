
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

Récupération de la pile d'appel
===============================

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
(lire `How do I write Flask's excellent debug log message to a file in production?
<http://stackoverflow.com/questions/14037975/how-do-i-write-flasks-excellent-debug-log-message-to-a-file-in-production>`_).

Message d'erreur plus explicite
===============================

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
qui permet d'ajouter une erreur sans perdre les informations l'exception originale.
Ce mécanisme est souvent utilisé pour donner plus d'information à l'utilisateur
de la fonction, plus que le message d'erreur initial.

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
            raise Exception(f"Issue with element {i} and log function.") from exc

La dernière partie de la dernière ligne est importante :
``from exc``. Le langage garde ainsi la trace de la première
exception.

Type d'exception
================

Le langage Python propose des types d'exceptions prédéfinis :
`Built-in Exceptions <https://docs.python.org/3/library/exceptions.html>`_.
Chaque type correspond à un type d'erreur particulier. Il est toujours préférable
d'attraper un type d'exception précis plutôt que le type générique `Exception`.
De cette façon, tout autre type d'exception sera toujours considéré comme une erreur.

.. runpython::
    :showcode:
    :exception:

    import math
    ensemble = [1, 0, 2]
    s = 0
    for i, e in enumerate(ensemble):
        try:
            s += math.log(e)
        except ValueError as exc:
            raise ValueError(f"Issue with element {i} and log function.") from exc

De la même manière, il est préférable en d'erreur de lancer une exception d'un type précis.
Plus le type est restrictif, plus l'information retournée au développeur utilisant la fonction
est précise et celui-ci peut choisir d'intercepter un type précis d'exception.

Conventions
===========

Si le programme ne peut continuer, il est d'usage de lancer une exception
avec un message d'erreur suffisamment explicite pour dire à celui qui
utilise le programme comment faire pour corriger le problème.
Pour ce faire, le message est important, le type d'exception aussi.

En règle générale, le programme ne continue pas après avoir lancé une exception.
Mais comme Python dispose d'un :epkg:`garbage collector`, l'interpréteur
se charge lui-même de détruire ce qui n'est plus nécessaire si l'utilisateur
du code fautif intercepte l'exception et continue l'exécution du programme.

::

    try:
        with open("file_to_read.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        # On continue malgré tout et on récupère les données
        # souhaitées autrement.
        content = download_content()

Toutefois il est préférable d'écrire ce qui suit car d'autres langages de programmation
sont moins permissifs.

::

    if os.path.exists("file_to_read.txt"):
        with open("file_to_read.txt", "r") as f:
            content = f.read()
    else:
        # On continue malgré tout et on récupère les données
        # souhaitées autrement.
        content = download_content()

Attraper une exception est parfois nécessaire si celle-ci se produit dans une
fonction dont le code n'est pas modifiable.

::

    try:
        content = read_fromf_file("file_to_read.txt")
    except FileNotFoundError:
        # On continue malgré tout et on récupère les données
        # souhaitées autrement.
        content = download_content()

Dans ce cas, même si le langage python détruit la plupart des variables
qui ne sont plus utilisées. Il n'en est pas toujours de même avec
des ressources comme un fichier, un accès internet...

::

    try:
        f = open(name, "r")
        content = f.read()  # l'erreur se produit ici
        f.close()
    except UnicodeEncodeError as e:
        # Le fichier contient un caractère inattendu.
        raise ValueError(f"Unable to read file {name!r}.") from e

Dans l'exemple précédent, le fichier `f` n'est pas jamais fermé.
L'utilisateur ne pourra pas le supprimer ou le réécrire
jusqu'à ce ce que `f.close()` soit exécuté ou l'interpréteur
python terminé.

.. runpython::
    :showcode:
    :exception:

    name = "essai.txt"
    with open(name, "w", encoding="utf-8") as f:
        f.write("ééééééé")

    try:
        f = open(name, "r", encoding="ascii")
        content = f.read()  # l'erreur se produit ici
        f.close()
    except UnicodeEncodeError as e:
        # Le fichier contient un caractère inattendu.
        print(f"unable to read file {name!r} ({e})")

    with open(name, "w", encoding="utf-8") as f:
        f.write("àààààààà")
