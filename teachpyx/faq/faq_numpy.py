# coding: utf-8
import numpy


def to_float32(x):
    """
    Convertit un nombre réel en nombre réel simple précision.

    .. faqref:
        :title: double ou float ?
        :tag: numpy

        :epkg:`numpy` est un module de calcul numérique.
        Comme tous les modules optimisés le pour calcul,
        il est écrit en partie en :epkg:`C++`. Ce language
        est plus bas niveau que :epkg:`Python`.
        :epkg:`numpy` propose différents types pour stocker des nombres
        `Array types and conversions between types <https://docs.scipy.org/doc/numpy/user/basics.types.html>`_.
        Pourquoi autant ? Parce que pour faire des calculs rapides, il faut utiliser
        le plus petit type possible. Les réels sont représentés selon deux types :
        `double <https://en.wikipedia.org/wiki/Double-precision_floating-point_format>`_
        codé sur 8 octets ou 64 bits et
        `float <https://en.wikipedia.org/wiki/Single-precision_floating-point_format>`_
        codé sur 4 octets ou 32 bits.
        Les premiers ont 15 chiffres de précisions, les seconds 7.
        En machine learning, la précision n'est pas nécessairement un critère
        de performances, c'est pourquoi beaucoup de librairies de
        *machine learning* implémente leurs calculs en *float*.
        Cela prend moins d'espace en mémoire, les calculs sont plus rapides.
        Le type *float* en :epkg:`Python` correspond à un *double* en :epkg:`C++`.
        Pour le convertir en nombre sur 32 bit, il faut utiliser :epkg:`numpy` :

        .. runpython::
            :showcode:

            import math
            print(math.pi)

            import numpy
            fpi = numpy.float32(math.pi)
            print(fpi)

        Est-ce qu'une fonction produit des résultats proches qu'elle
        utilise des *float* ou des *double* ? C'est une bonne question
        et la réponse est oui si elle est continue. Si elle ne l'est pas,
        le résultat est parfois imprévisible. Pour en savoir
        plus : :ref:`floatanddoubleroudingrst`.
    """
    return numpy.float32(x)
