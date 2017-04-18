
.. _chap_dates:

=====
Dates
=====

.. contents::
    :local:
    :depth: 2

datetime
========

Le module `datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime>`_
fournit une classe `datetime https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime>`_
qui permet de faire des opérations et des comparaisons sur les dates et les heures.
L'exemple suivant calcule l'âge d'une personne née le 11 août 1975.

.. runpython::
    :showcode:

    import datetime
    naissance = datetime.datetime (1975, 11, 8, 10, 0, 0)
    jour = naissance.now () # obtient l'heure et la date actuelle
    print(jour)             # affiche quelque chose comme 2017-05-22 11:24:36.312000
    age = jour - naissance  # calcule une différence
    print(age)              # affiche 12614 days, 1:25:10.712000

L'objet `datetime https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime>`_
autorise les soustractions et les comparaisons entre deux dates. Une soustraction
retourne un objet de type
`timedelta https://docs.python.org/3/library/datetime.html?highlight=timedelta#datetime.timedelta>`_
qui correspond à une durée qu'on peut multiplier par un réel ou ajouter à un
objet de même type ou à un objet de type
`datetime https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime>`_.
L'utilisation de ce type d'objet évite de se pencher sur tous les problèmes de conversion.

Le module `calendar <https://docs.python.org/3/library/calendar.html?highlight=calendar#module-calendar>`_
est assez pratique pour construire des calendriers. Le programme ci-dessous
affiche une liste de t-uples incluant le jour et le jour de la semaine du
mois d'août 1975. Dans cette liste, on y trouve le t-uple ``(11,0)``
qui signifie que le 11 août 1975 était un lundi. Cela permet de récupérer
le jour de la semaine d'une date de naissance.

.. runpython::
    :showcode:

    import calendar
    c = calendar.Calendar ()
    for d in c.itermonthdays2(1975, 8):
        print(d)

Autres formats de date
======================

La date d'un événement est constamment utilisée,
la date de modification d'un fichier par exemple pour détecter
que celui-ci a été modifié depuis sa synchronisation avec un site web
par exemple. On appelle ces dates associées à des événements
des `timestamp <https://fr.wikipedia.org/wiki/Horodatage>`_.
Ce sont des nombres entiers qui expriment le nombre de secondes
qui se sont écoulées depuis une certaine origine qui
dépend du système d'exploitation. C'est un nombre réel : 
la partie entière est un nombre de seconde, la partie décimale 
donne les millisecondes. La valeur n'a pas de sens exploitable
à moins de la convertir en un format compréhensible.
C'est ce que fait la fonction 
`fromtimestamp <https://docs.python.org/3/library/datetime.html?highlight=fromtimestamp#datetime.datetime.fromtimestamp>`_.

.. runpython::
    :showcode:
    
    import time
    ts = time.time()
    print(ts)
    
    import datetime
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(st)

