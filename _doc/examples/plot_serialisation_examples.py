# coding: utf-8
"""
=============
Sérialisation
=============

Le notebook explore différentes façons de sérialiser des données et leurs limites.

JSON
====

Le format :epkg:`JSON` est le format le plus utilisé sur internet
notemmant via les :epkg:`API REST`.

Ecriture (json)
+++++++++++++++
"""
from io import StringIO, BytesIO
import timeit
import json
import numpy
import ujson
import cloudpickle
import pickle


data = {
    "records": [
        {
            "nom": "Xavier",
            "prénom": "Xavier",
            "langages": [{"nom": "C++", "age": 40}, {"nom": "Python", "age": 20}],
        }
    ]
}


#########################################
#

buffer = StringIO()
res = json.dump(data, buffer)  # 1
seq = buffer.getvalue()
seq


#########################################
# Lecture (json)
# ++++++++++++++


buffer = StringIO(seq)
read = json.load(buffer)
read


#########################################
# Limite
# ++++++
#
# Les matrices :epkg:`numpy` ne sont pas sérialisables facilement.


data = {"mat": numpy.array([0, 1])}

buffer = StringIO()
try:
    json.dump(data, buffer)
except Exception as e:
    print(e)


#########################################
# Les classes ne sont pas sérialisables non plus facilement.


class A:
    def __init__(self, att):
        self.att = att


data = A("e")
buffer = StringIO()
try:
    json.dump(data, buffer)
except Exception as e:
    print(e)


#########################################
# Pour ce faire, il faut indiquer au module :mod:`json`
# comment convertir la classe en un ensemble de listes et dictionnaires et
# la classe :class:`json.JSONEncoder`.


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return {"classname": o.__class__.__name__, "data": o.__dict__}


data = A("e")
buffer = StringIO()
res = json.dump(data, buffer, cls=MyEncoder)
res = buffer.getvalue()
res

#########################################
# Et la relecture avec la classe :class:`json.JSONDecoder`.


class MyDecoder(json.JSONDecoder):
    def decode(self, o):
        dec = json.JSONDecoder.decode(self, o)
        if isinstance(dec, dict) and dec.get("classname") == "A":
            return A(dec["data"]["att"])
        else:
            return dec


buffer = StringIO(res)
obj = json.load(buffer, cls=MyDecoder)
obj


#########################################
# Sérialisation rapide
# ++++++++++++++++++++
#
# Le module :mod:`json` est la librairie standard de Python mais comme
# la sérialisation au format *JSON* est un besoin très fréquent,
# il existe des alternative plus rapide comme :epkg:`ujson`.


data = {
    "records": [
        {
            "nom": "Xavier",
            "prénom": "Xavier",
            "langages": [{"nom": "C++", "age": 40}, {"nom": "Python", "age": 20}],
        }
    ]
}


#########################################
#


timeit.timeit("json.dump(data, StringIO())", globals=globals(), number=100)


#########################################
#


timeit.timeit("ujson.dump(data, StringIO())", globals=globals(), number=100)


#########################################
# Ces deux lignes mesures l'écriture au format JSON
# mais il faut aussi mesurer la lecture.


buffer = StringIO()
ujson.dump(data, buffer)
res = buffer.getvalue()
timeit.timeit("json.load(StringIO(res))", globals=globals(), number=100)


#########################################
#

timeit.timeit("ujson.load(StringIO(res))", globals=globals(), number=100)


#########################################
# On enlève le temps passé dans la creation du buffer.


timeit.timeit("StringIO(res)", globals=globals(), number=100)


#########################################
# Pickle
# ======
#
# Le module :mod:`pickle` effectue la même chose mais au format binaire.
# Celui-ci est propre à *Python* et ne peut être lu d'autres langages,
# voire parfois par d'autres versions de *Python*.
#
# Ecriture (pickle)
# +++++++++++++++++


data = {
    "records": [
        {
            "nom": "Xavier",
            "prénom": "Xavier",
            "langages": [{"nom": "C++", "age": 40}, {"nom": "Python", "age": 20}],
        }
    ]
}


#########################################
#


buffer = BytesIO()
res = pickle.dump(data, buffer)
seq = buffer.getvalue()
seq


#########################################
# Lecture (pickle)
# ++++++++++++++++


buffer = BytesIO(seq)
read = pickle.load(buffer)
read


#########################################
# Les classes
# +++++++++++
#
# A l'inverse du format *JSON*, les classes sont sérialisables avec
# :mod:`pickle` parce que le langage utilise un format très proche
# de ce qu'il a en mémoire. Il n'a pas besoin de conversion supplémentaire.


data = A("r")
buffer = BytesIO()
res = pickle.dump(data, buffer)
seq = buffer.getvalue()
seq


#########################################
#

buffer = BytesIO(seq)
read = pickle.load(buffer)
read


#########################################
# Réduire la taille
# +++++++++++++++++
#
# Certaines informations sont duppliquées et il est préférable de ne pas
# les sérialiser deux fois surtout si elles sont voluminueuses.


class B:
    def __init__(self, att):
        self.att1 = att
        self.att2 = att


#########################################
#

data = B("r")
buffer = BytesIO()
res = pickle.dump(data, buffer)
seq = buffer.getvalue()
seq


#########################################
# Evitons maintenant de stocker deux fois le même attribut.


class B:
    def __init__(self, att):
        self.att1 = att
        self.att2 = att

    def __getstate__(self):
        return dict(att=self.att1)


data = B("r")
buffer = BytesIO()
res = pickle.dump(data, buffer)
seq = buffer.getvalue()
seq


#########################################
# C'est plus court mais il faut inclure maintenant la relecture.


class B:
    def __init__(self, att):
        self.att1 = att
        self.att2 = att

    def __getstate__(self):
        return dict(att=self.att1)

    def __setstate__(self, state):
        setattr(self, "att1", state["att"])
        setattr(self, "att2", state["att"])


buffer = BytesIO(seq)
read = pickle.load(buffer)
read


#########################################
#

read.att1, read.att2


#########################################
#

data = B("r")
timeit.timeit("pickle.dump(data, BytesIO())", globals=globals(), number=100)


#########################################
#

timeit.timeit("pickle.load(BytesIO(seq))", globals=globals(), number=100)


#########################################
# La sérialisation binaire est habituellement plus rapide dans les langages
# bas niveau comme C++. La même comparaison pour un langage haut niveau
# tel que Python n'est pas toujours prévisible.
# Il est possible d'accélérer un peu les choses.


timeit.timeit(
    "pickle.dump(data, BytesIO(), protocol=pickle.HIGHEST_PROTOCOL)",
    globals=globals(),
    number=100,
)


#########################################
# Cas des fonctions
# =================
#
# La sérialisation s'applique à des données et non à du code mais le
# fait de sérialiser des fonctions est tout de même tentant.
# La sérialisation binaire fonctionne même avec les fonctions.
#
# Binaire
# +++++++


def myfunc(x):
    return x + 1


data = {"x": 5, "f": myfunc}


buffer = BytesIO()
res = pickle.dump(data, buffer)
buffer.getvalue()


#########################################
#


res = pickle.load(BytesIO(buffer.getvalue()))
res


#########################################
#

res["f"](res["x"])


#########################################
# La sérialisation ne conserve pas le code de la fonction, juste son nom.
# Cela veut dire que si elle n'est pas disponible lorsqu'elle est appelée,
# il sera impossible de s'en servir.


del myfunc


try:
    pickle.load(BytesIO(buffer.getvalue()))
except Exception as e:
    print(e)


#########################################
# Il est possible de contourner l'obstacle en utilisant le module
# :epkg:`cloudpickle` qui stocke le code de la fonction.


def myfunc(x):
    return x + 1


data = {"x": 5, "f": myfunc}


buffer = BytesIO()
res = cloudpickle.dump(data, buffer)
buffer.getvalue()


#########################################
#

del myfunc


res = cloudpickle.load(BytesIO(buffer.getvalue()))
res


#########################################
#

res["f"](res["x"])


#########################################
# Fonction et JSON
# ++++++++++++++++
#
# La sérialisation d'une fonction au format JSON ne
# fonctionne pas avec le module standard.


buffer = StringIO()
try:
    json.dump(data, buffer)  # 2
except Exception as e:
    print(e)


#########################################
# La sérialisation avec :epkg:`ujson` ne fonctionne pas non plus
# même si elle ne produit pas toujours d'erreur.


buffer = StringIO()
try:
    res = ujson.dump(data, buffer)  # 3
except TypeError as e:
    print(e)
buffer.getvalue()


#########################################
# Cas des itérateurs
# ==================
#
# Les itérateurs fonctionnent avec la sérialisation binaire mais ceci
# implique de stocker l'ensemble que l'itérateur parcourt.


ens = [1, 2]

data = {"x": 5, "it": iter(ens)}


buffer = BytesIO()
res = pickle.dump(data, buffer)  # 4
buffer.getvalue()


#########################################
#

del ens

res = pickle.load(BytesIO(buffer.getvalue()))
res


#########################################
#

list(res["it"])


#########################################
#

list(res["it"])


#########################################
# Cas des générateurs
# ===================
#
# Ils ne peuvent être sérialisés car le langage n'a pas accès à l'ensemble
# des éléments que le générateur parcourt. Il n'y a aucun moyen de
# sérialiser un générateur mais on peut sérialiser la fonction qui crée le générateur.


def ensgen():
    yield 1
    yield 2


data = {"x": 5, "it": ensgen()}


buffer = BytesIO()
try:
    pickle.dump(data, buffer)
except Exception as e:
    print(e)
