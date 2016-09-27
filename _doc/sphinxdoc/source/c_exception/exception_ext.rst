

.. _l-exception-ext:

=====
Usage
=====

Pile d'appel
============


Récupération de la pile  d'appel
++++++++++++++++++++++++++++++++

Le module `traceback <https://docs.python.org/3/library/traceback.html>`_
permet de récupérer la pile d'appels lorsqu'une exception survient.

::

    def raise_exception():
        raise Exception("an error was raised")
            
    try:
        insidefe()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("".join(traceback.format_tb(exc_traceback)))
        
Le programme affiche :

::

    File "test_faq_exception.py", line 57, in raise_exception
      raise Exception("an error was raised")

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

::

    import math
    ensemble = [1, 0, 2]
    s = 0
    for e in ensemble:
        s += math.log(e)

::

    Traceback (most recent call last):
      File "i.py", line 5, in <module>
        s += math.log(e)
    ValueError: math domain error
    
Typiquement dans ce cas précis, on ne sait pas quel est l'indice
de l'élément qui a provoqué l'erreur. On utilise alors un mécanisme
qui permet d'ajouter une erreur sans perdre les informations l'exception original

::

    import math
    ensemble = [1, 0, 2]
    s = 0
    for i, e in enumerate(ensemble):
        try:
            s += math.log(e)
        except Exception as exc:
            raise Exception("Issue with element {0}".format(i)) from exc

La dernière partie de la dernière ligne est importante : ``from exc``.
Le langage garde ainsi la trace de la première exception.

::

    Traceback (most recent call last):
      File "i.py", line 6, in <module>
        s += math.log(e)
    ValueError: math domain error

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "i.py", line 8, in <module>
        raise Exception("Issue with element {0}".format(i)) from exc
    Exception: Issue with element 1



Conventions
===========

Erreur ou code d'erreur
+++++++++++++++++++++++

.. todoext::
    :title: terminer la section Erreur ou code d'erreur
    
    parler aussi de coûts d'une exception,
    libération des ressources
