
============
Introduction
============

Ceci est une relecture du livre que j'ai écrit en 2009
`Programmation avec le langage Python
<https://www.editions-ellipses.fr/accueil/3823-programmation-avec-le-langage-python-2e-edition-9782729863371.html>`_
écrit en 2011 avec une version de Python que plus personne n'utilise.
La transcription du livre sous la forme d'un site web et d'un
module python a permis d'automatiser la vérification des exemples
pour assurer que ceux-ci fonctionnent encore avec les dernières
versions du langage et de ses dépendances.

Installation de Python
======================

Pour ceux qui débutent, je recommande l'utilisation de la
distribution :epkg:`Anaconda`. Elle fonctionne sous Windows,
Linux, MacOS.
Pour ceux qui souhaitent réduire la taille
du premier téléchargement (> 500 Mo), elle existe en version
allégée :epkg:`Miniconda`. Avec cette distribution, il est quasiment
possible de tout faire grâce à une interface graphique.
Comme ce n'est pas la version officielle, cette distribution
est mise à jour avec quelques semaines ou mois de retard
par rapport à cette dernière. C'est rarement un problème.

En ce qui me concerne, je préfère la version officielle de :epkg:`Python`.
Elle est moins gourmande sur le disque mais parfois plus
difficile à maîtriser lors de l'installation de certaines
extensions. Elle est installée par défault sur les distributions Linux.

Installation d'extensions ou modules ou packages
================================================

Le langage Python est un langage de programmation qui seul ne permet
pas de faire grand chose hormis des calculs simples. Heureusement,
des extensions existent pour le compléter et faire du calcul
numérique, créer des sites webs, accéder à d'autres applications
comme Excel. Ces extensions sont partagées sur le site officiel
:epkg:`pypi`. Elles sont trop nombreuses mais certains sites prennent
le temps de créer une sorte de florilège : :epkg:`Awesome Python`.
Pour installer une extension, il suffit de d'écrire sur une ligne
de commande :

::

    pip install <extension>

Si vous utilisez la distribution :epkg:`Anaconda` ou :epkg:`Miniconda`,
il est préférable d'essayer d'abord :

::

    conda install <extension>

Des exemples de codes sont d'ailleurs disponibles sous la forme d'un module python.

::

    pip install teachpyx

Accents
=======

Le langage :epkg:`python` est conçu pour un monde anglophone
et l'utilisation des accents ne va pas de soi.
Le programme suivant qui demande d'afficher un message
contenant un accent peut provoquer l'apparition d'une erreur
selon les caractéristiques de votre machine.

::

    print("accentué")

L'erreur est la suivante :

::

    File "essai.py", line 1
    SyntaxError: Non-ASCII character '\xe9' in file i.py on line 1,
             but no encoding declared;
             see https://peps.python.org/pep-0263/ for details

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
A cause des accents, les exemples cités dans ce
livre ne fonctionnent pas toujours sans cette première ligne qui a
parfois été enlevée pour des questions
de lisibilité. Il faut penser à l'ajouter pour reproduire
les exemples.

Les dernières versions du langage Python autorisent maintenant la
présence de lettres accentuées dans les noms des variables, de fonctions
ou de classes. Néanmoins, c'est une mauvaise habitude à prendre
car beaucoup de langages ne le permettent pas.

L'instruction ``print(...)`` ordonne à l'ordinateur d'afficher
un message à l'écran. Il n'a aucun impact sur son fonctionnement.
Elle est beaucoup utilisée pour vérifier que le programme
fait bien ce qu'il est supposé faire.

Une nouvelle version du langage Python est maintenant publiée chaque année.
L'ensemble des modifications est tenue à jour sur la page 
`Python Enhancement Proposals (PEP) <https://peps.python.org/>`_.
Chaque version est maintenue environ cinq ans selon un calendrier
précisé au moment de la sortie.

Trois concepts, séquence, test, boucle
======================================

.. index:: séquence, test, boucle

La programmation autre que quantique s'appuient sur trois concepts simples.
Tout programme est un assemblage souvent complexe de ceux-ci.
Le premier est la **séquence**. Par défaut, l'ordinateur enchaîne
les instructions.

::

    a = 1       # affecte 1 à a
    b = a + 5   # affecte a + 5 à b

`a` et `b` sont des variables. Elles permettent de manipuler
des informations, ici, des nombres. Les nommer permet d'écrire
des instructions qui ne dépendent plus des informations auxquelles
elles sont associées.

Le second concept est le **test**. C'est la capacité de choisir
une direction plutôt qu'une autre. Le programme suivant compare
la valeur associée à la variable `a`. Si elle est supérieur
à 1 alors `b` reçoit la `1 + 5`, sinon `b` reçoit `1 + 6`.

::

    if a > 1:
        b = 1 + 5
    else:
        b = 1 + 6

Le troisième concept est la **boucle**. C'est la capacité de
répéter la même séquence d'instructions. L'exemple suivant
répète 10 fois la même instructions qui consiste à ajouter
deux nombres. Le résultat est la somme des 10 premiers
entiers.


::

    a = 0                     # initialisation
    for i in range(1, 11):    # pour i allant de 1 à 11 exclu
        a = a + i             # on ajoute i à a

Excepté pour la programmation quantique, ces trois concepts sont identiques
dans tous les langages relevant de la :epkg:`programmation impérative`
ou de la :epkg:`programmation fonctionnelle`, soit tous ceux qui existent
aujourd'hui.

Algorithmes
===========

Pour simplifier, un :epkg:`algorithme` est un assemblage
fini de ces trois concepts. On peut se dire que la tâche est
immense lorsqu'on commence à programmer mais il existe déjà
de nombreux algorithmes. Le plus souvent,
un programme réutilise beaucoup de choses existantes, et ajoute
le peu qui est nécessaire à son auteur pour faire la tâche
pour laquelle il l'écrit. Il est rare que quelqu'un dans le monde
entier n'ait pas déjà réfléchi au problème que vous vous posez.
Le travail consiste d'abord à chercher ce qui existe puis
de voir les bouts qui manquent pour assembler ce qu'on a trouvé.

Les :epkg:`algorithmes numériques` sont généralement
ceux qu'on qualifie d'algorithmes. Tout l'enjeu est faire
des calculs le plus rapidement possibles et pour un grand
nombres de problèmes, il existe déjà un algorithme optimal,
pour lequel on sait qu'il n'existe pas de version plus rapide.
L'algorithme le plus connu est celui du tri, il existe
d'ailleurs plusieurs :epkg:`algorithmes de tri`.
On programme plus vite quand on connaît déjà quelques-uns
de ces algorithmes. Cette culture algorithmique est encore
rarement abordée à l'école bien que la programmation fasse
partie du cursus scolaire. Ces algorithmes sont aussi intemporels.
Ils continueront d'exister jusqu'à la nuit des temps au même
titre que les mathématiques.

Les autres algorithmes couvrent tous les autres besoins,
comme ceux d'accéder à une ressource comme internet, une
base de données, un serveur de mail, une autre application
comme Excel. Cette partie évolue rapidement. Il n'est pas rare
d'en réécrire une partie tous les cinq ou dix ans parce qu'un
outil a changé comme une base de données, la sécurité a changé,
l'endroit où les données sont stockées...

La suite du site se lit en diagonale ou en rang serré selon vos
connaissances actuelles, selon que vous connaissez déjà un
autre langage de programmation. Et il faut pratiquer.

Fichier ou notebook
===================

Il faut bien écrire son programme quelque part. Il exite deux options.
La première est d'écrire son programme dans un fichier texte
qui doit obligatoirement avoir l'extension ``.py``. On peut ensuite
l'exécuter avec l'instruction en ligne de commande
``python <nom de fichier.py>``. Il est recommandé d'utiliser
un éditeur de texte dédié à cet usage. Le plus utilisé est
:epkg:`Visual Studio Code`.

La seconde option est un notebook. Cette façon de travailler
nécessite l'installation de :epkg:`jupyter`. C'est plus facile
quand on commence. Ce support vise principalement les chercheurs
qui peuvent de cette façon avoir dans un même document
du code, des sorties de code, du texte, des formules, des graphiques.
C'est déconseillé dès qu'on doit utiliser un programme pour automatiser
une tâche.
