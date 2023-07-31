
###############
Parallélisation
###############

.. index:: GIL, Global Lock Interpreter

Le langage Python propose plusieurs façons de paralléliser un traitement
sans faire appel à des librairies extérieures. C'est ce que propose d'aborder
les paragraphes suivantes.

.. toctree::
    :maxdepth: 2

    thread

.. index:: asyncio, uvloop, gevent

Il existe d'autres librairies qui ont été développés pour des usages
spécifiques telles que
`joblib <https://joblib.readthedocs.io/en/stable/>`_ qui est utilisé
par `scikit-learn <http://scikit-learn.org/stable/>`_.
La librairie `gevent <http://www.gevent.org/>`_ est un équivalent
de la librairie :mod:`asyncio`
qui a été intégrée à Python 3.4. Plus récemment, le package
`uvloop <https://uvloop.readthedocs.io/user/index.html>`_
propose une accélération de deux à quatre fois par rapport à la librairie
:mod:`asyncio` :
`uvloop: Blazing fast Python networking <https://magic.io/blog/uvloop-blazing-fast-python-networking/>`_.
Cette dernière librairie est utilisée par le module
`sanic <http://sanic.readthedocs.io/en/latest/>`_ qui implémenté
un serveur web plus rapide que
`flask <http://flask.pocoo.org/>`_.
La page `Parallel Processing in Python
<https://www.machinelearningplus.com/python/parallel-processing-python/>`_
passe en revue différentes stratégies de parallélisation
pour l'implémentation de calculs numériques avec
:epkg:`joblib`, :epkg:`cython`, :epkg:`OpenMP`.
