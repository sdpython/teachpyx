
============
Introduction
============

Ceci est une relecture du livre que j'ai écrit en 2009
`Programmation avec le langage Python <http://www.editions-ellipses.fr/product_info.php?products_id=6891>`_
et disponible au format `PDF <http://www.xavierdupre.fr/site2013/index_documents.html>`_.
Internet est le média le plus utilisé quant il s'agit d'apprendre à programmer
et un module Python est plus pratique pour s'assurer qu'un code Python reste valide
lors du passage à une nouvelle version du langage.

**Installation**

Les exemples de codes sont disponibles sous la forme d'un module python
et des :ref:`notebooks <l-notebooks>` accessibles sur le site.

::

    pip install teachpyx

.. _par_intro_accent_code:

Le langage :epkg:`python` est conçu pour le monde anglophone
et l'utilisation des accents ne va pas de soi.
Le programme suivant qui demande d'afficher un message
contenant un accent provoque l'apparition d'une erreur :

::

    print("accentué")

L'erreur est la suivante :

::

    File "essai.py", line 1
    SyntaxError: Non-ASCII character '\xe9' in file i.py on line 1,
             but no encoding declared;
             see http://www.python.org/peps/pep-0263.html for details

Dans ce cas, il faut ajouter une ligne placée en première position
qui précise que des accents pourront être utilisés.
L'exécution du programme qui suit ne soulève aucune erreur.

::

    # coding: utf-8
    print("accentué")

Cette ligne précise en fait que l'interpréteur :epkg:`python`
doit utiliser un jeu de caractères spécial. Ces jeux de caractères
ont parfois leur importance, les navigateurs n'aiment pas trop
les accents au sein des adresses Internet : il est parfois
préférable de ne pas utiliser d'accents sur les sites de
réservations d'hôtels, de trains ou d'avions même si aujourd'hui
ce problème ne devrait plus en être un. Dans le cas contraire,
cela donne une indication du côté vieillot voire obsolète
d'une implémentation.
A cause des accents, la plupart des exemples cités dans ce
livre ne fonctionnent pas sans cette première ligne qui a
parfois été enlevée pour des questions
de lisibilité. Il faut penser à l'ajouter pour reproduire
les exemples.
Sur Internet, on trouve de nombreux exemples commençant
par la ligne suivante :

::

    #!/usr/local/bin/python

On rencontre souvent cette ligne pour un programme écrit
sur une machine :epkg:`Linux`, elle indique l'emplacement
de l'interpréteur :epkg:`python` à utiliser. Cette ligne
s'appelle un :epkg:`shebang`.
