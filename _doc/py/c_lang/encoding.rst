
.. _chap_encoding:

==============================
Encoding et jeux de caractères
==============================

.. index:: jeux de caractères

Jeux de caractères
==================

La langue anglaise est la langue dominante en ce qui concerne l'informatique
mais cela n'empêche pas que des programmes anglais manipulent du japonais
même si le nombre de caractères est beaucoup plus grand. Les caractères les plus
fréquent peuvent être représentés par un octet, soit au plus 256 caractères.
Lorsque la langue en contient plus, il faut utiliser plusieurs octets pour un caractères.
C'est à ça ce que servent les jeux de caractères : ils définissent la
façon de passer d'une suite d'octets à une séquence de caractères
et réciproquement.
Pour être plus précis, le jeu de caractère désigne l'ensemble de caractères
dont le programme a besoin, l'encodage décrit la manière dont on passe d'une séquence
de caractères français, japonais, anglais à une séquence d'octets qui est
la seule information manipulée par un ordinateur. Le décodage définit le passage inverse.
Les langues latines n'ont besoin
que d'un octet pour coder un caractère, les langues asiatiques en ont besoin
de plusieurs. Il n'existe pas qu'un seul jeu de caractères lorsqu'on
programme. Ils interviennent à plusieurs endroits différents :

* Le jeu de caractères utilisé par l'éditeur de texte pour afficher le programme.
* Le jeu de caractères du programme, par défaut `ascii <https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange>`_
  mais il peut être changé en insérant une première ligne de commentaire (exemple : ``# -*- coding: utf-8 -*-``).
  Les chaînes de caractères du programme sont codées avec ce jeu de caractères.
  Ce jeu devrait être identique à celui utilisé par l'éditeur de texte afin d'éviter
  les erreurs.
* Le jeu de caractères de la sortie, utilisé pour chaque instruction ``print``,
  il est désigné par le code `cp1252 <https://fr.wikipedia.org/wiki/Windows-1252>`_
  sur un système *Windows*.
* Le jeu de caractères dans lequel les chaînes de caractères sont manipulées.
  Un jeu standard qui permet de représenter toutes les langues est le jeu de
  caractères `utf-8 <https://fr.wikipedia.org/wiki/UTF-8>`_.
  Il peut être différent pour chaque variable.
* Le jeu de caractères d'un fichier texte. Il peut être différent pour chaque fichier.

Depuis la version 3 de *Python*, toutes les chaînes de caractères sont au format
`unicode <https://fr.wikipedia.org/wiki/Unicode>`_. C'est à dire que le jeu de caractères
est le même pour toutes les chaînes de caractères. Pour en changer, il faut *encoder*
le texte avec un jeu spécifique et la fonction
`encode <https://docs.python.org/3/library/stdtypes.html?highlight=encode#str.encode>`_.
Il deviendra une chaîne d'octets ou
`bytes <https://docs.python.org/3/library/functions.html?highlight=bytes#bytes>`_.
La transformation inverse s'effectue avec la méthode
`decode <https://docs.python.org/3/library/stdtypes.html?highlight=encode#bytes.decode>`_.

.. runpython::
    :showcode:

    st = "eé"
    print(type(st))
    print(len(st))

    sb = st.encode("latin-1")
    print(type(sb))
    print(len(sb))

L'exemple précédent montre que la fonction `len <https://docs.python.org/3/library/functions.html?highlight=len#len>`_
retourne le nombre de caractères mais cela ne correspond pas au nombre d'octets que cette chaîne
occupe en mémoire.

.. runpython::
    :showcode:

    st = "eé"
    print(type(st))
    print(len(st))

    sb = st.encode("utf-16")
    print(type(sb))
    print(len(sb))

Un autre jeu, une autre longueur.

Fichiers
========

Comme *Python* utilise un jeu unique, il suffit de faire attention où on récupère
les chaînes de caractères et au moment où on les transfère. C'est ce qu'on appelle les
entrées sorties comme lire ou écrire un fichier.
Par défaut un fichier est écrit avec le jeu de caractères du système d'exploitation.
Pour un préciser un autre, il faut spécifier le paramètre *encoding*.
Toutes les chaînes de caractères seront lues et converties au format *unicode* depuis ou vers
l'encoding spécifié.

::

    with open("essai.txt", "r", "utf-8") as f:
        text = f.read()

Méthodes
========

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - ``encode( [enc[,err]])``
      - Cette fonction permet de passer d'un jeu de caractères, celui de la variable, au jeu de caractères
        précisé par *enc* à moins que ce ne soit le jeu de caractères par défaut.
        Le paramètre *err* permet de préciser comment gérer les erreurs, doit-on
        interrompre le programme (valeur ``'strict'`` ou les ignorer (valeur ``'ignore'``).
        La documentation *Python* recense toutes les valeurs possibles pour ces deux paramètres aux adresses
    * - ``decode([enc[, err]]``
      - Cette fonction est la fonction inverse de la fonction ``encode``.
        Avec les mêmes paramètres, elle effectue la transformation inverse.

Encodings par défaut
====================

Le programme suivant permet d'obtenir le jeu de caractères par
défaut et celui du système d'exploitation.

.. runpython::
    :showcode:

    import sys
    import locale
    import platform
    print(sys.platform)
    print(platform.architecture)
    print(sys.getdefaultencoding())
    print(locale.getdefaultlocale())

Les problèmes d'encoding surviennent parfois car on précise
rarement l'encoding du programme *Python* ni le programmeur ne contrôle
pas facilement celui de la sortie (``print``). Ces deux paramètres changent
selon les éditeurs ou les systèmes d'exploitations.
