
.. _l-warning:

==================
Warning et logging
==================

.. index:: warning

Warnings
========

Les *warnings* ne sont pas des erreurs mais des soupçons d'erreurs.
Le programme peut continuer mais il est possible qu'il s'arrête
un peu plus tard et la cause pourrait être un *warning* déclenché
un peu plus tôt.

Un des *warning* les plus utilisé est le
`DeprecationWarning <https://docs.python.org/3/library/warnings.html#warning-categories>`_
qui indique que le code utilisé va disparaître sous cette forme
lors des prochaines release. :epkg:`scikit-learn` suit la règle suivante
à chaque fois qu'une API change, un *warning* subsiste pendant deux release
pour une fonction appelée à disparaître. Le *warning*
apparaît à chaque fois qu'elle est exécutée, puis la fonction est
finalement supprimée. Tout code s'appuyant encore sur cette fonction
provoquera une erreur.

Générer un warning
------------------

Le module :mod:`warnings` permet de lancer un *warning* comme ceci :

.. runpython::
    :showcode:

    import warnings
    warnings.warn("Warning lancé !")

Il est préférable d'ailleurs de spécifier un type précis de
*warning* qui indique à l'utilisateur à quel type d'erreur
il s'expose sans avoir à lire le message, voire plus tard de
les trier.

.. runpython::
    :showcode:

    import warnings
    warnings.warn("Warning d'un certain lancé !", UserWarning)

Intercepter un warning
----------------------

Les *warning* sont parfois très agaçants car il s'insère dans les
sorties du programme qui deviennent moins lisibles. Il serait
préférable de les corriger mais ils surviennent parfois dans un module
qui n'a pas pris en compte l'évolution d'une de ses dépendances.
Il est difficile de corriger cette erreur immédiatement
à moins de modifier le code du module installé, ce qui n'est souvent
pas souhaitable voire impossible si ce module est écrit en :epkg:`C++`.
Le plus simple reste de les intercepter.

.. runpython::
    :showcode:

    import warnings

    def fxn():
        warnings.warn("deprecated", DeprecationWarning)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fxn()

On peut également intercepter un type particulier
de *warning*, c'est le rôle de la classe
`catch_warnings <https://docs.python.org/3/library/warnings.html#warnings.catch_warnings>`_ :

.. runpython::
    :showcode:

    import warnings

    def fxn():
        warnings.warn("deprecated", DeprecationWarning)

    print("Boucle 1")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        fxn()

    print("Boucle 2")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        fxn()

    print("Boucle 3")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        warnings.simplefilter("ignore", UserWarning)
        fxn()

.. index:: test unitaire

Il est parfois utile de mémoriser les *warning* généré par un
programme, c'est nécessaire principalement lorsqu'on écrit
des tests unitaires.

.. runpython::
    :showcode:

    import warnings

    def fxn():
        warnings.warn("deprecated", DeprecationWarning)

    with warnings.catch_warnings(record=True) as ws:
        warnings.simplefilter("always")
        fxn()

        print("nombre de warnings :", len(ws))

        for i, w in enumerate(ws):
            print("warning {0} : {1}".format(i, w))

Warning personnalisé
--------------------

Comme pour les exceptions, il est possible de définir ses propres
*warning* en héritant d'un *warning* en particulier.

.. runpython::
    :showcode:

    import warnings

    class MonWarning(UserWarning):
        pass

    warnings.warn("mon warning", MonWarning)

Logging
=======

Les logs enregistrent des événements qu'un programme produit.
Ils sont utilisées pour comprendre des erreurs que celui-ci produit.
Le premier réflexe est d'insérer des instructions `print` pour
afficher des résultats intermédiaires pour déterminer le premier
endroit où une erreur se produit. Et puis on les enlève car ils
rendent les résultats illisibles dans une masse d'informations
inutiles lorsque tout se passe bien.

Il faut voir les logs comme des `print` silencieux qu'un développeur
peut activer s'il a besoin de traces d'exécution pour débugger.
C'est aussi pratique pour comprendre ce qu'il se passe sur un problème
créer par un utilisateur d'un programme qu'on développe. L'utilisateur
peut activer les logs et les transmettre à celui qui peut les comprendre.
Les logs sont indispensables à tout site web. Ils enregistrent toutes les
connexions et permettent vérifier rapidement si un site est attaqué ou pas.

Les logs sont une fonctionnalité présente dans la plupart des langages.
En python, c'est le module :mod:`logging` qui l'implémente.
