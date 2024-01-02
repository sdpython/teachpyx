# coding: utf-8
import numpy


def numpy_matrix2list(mat):
    """
    Convertit une matrice :epkg:`numpy` en list.

    :param mat: matrix
    :return: liste de listes

    .. exref::
        :title: opérations avec numpy.matrix
        :tag: numpy

        Voici quelques écritures classiques avec le module
        :epkg:`numpy`.

        ::

            import numpy as np
            mat = np.matrix ( [[1,2],[3,4]] ) # crée une matrice 2*2
            s   = mat.shape           # égale à (nombre de lignes, nombre de colonnes)
            l   = mat [0,:]           # retourne la première ligne
            c   = mat [:,0]           # retourne la première colonne
            iv  = mat.I               # inverse la matrice
            mat [:,0] = mat [:,1]     # la première ligne est égale à la seconde
            o   = np.ones ( (10,10) ) # crée un matrice de 1 10x10
            d   = np.diag (mat)       # extrait la diagonale d'une matrice
            dd  = np.matrix (d)       # transforme d en matrice
            t   = mat.transpose ()    # obtient la transposée
            e   = mat [0,0]           # obtient de première élément
            k   = mat * mat           # produit matriciel
            k   = mat @ mat           # produit matriciel à partir de Python 3.5
            m   = mat * 4             # multiplie la matrice par 4
            mx  = np.max (mat [0,:])  # obtient le maximum de la première ligne
            s   = np.sum (mat [0,:])  # somme de la première ligne


            mat = np.diagflat ( np.ones ( (1,4) ) )
            print (mat)  # matrice diagonale
            t   =  mat == 0
            print (t)    # matrice de booléens
            mat [ mat == 0 ] = 4
            print (mat)  # ...
            print (iv)  # ...
    """
    return mat.tolist()


def numpy_types():
    """
    Returns the list of numpy available types.

    :return: list of types

    To know a little bit more about those types.

    .. faqref::
        :title: Quels sont les types que numpy supporte ?
        :tag: numpy

        Lire `basic types
        <http://docs.scipy.org/doc/numpy/user/basics.types.html>`_.
        `numpy <http://docs.scipy.org/doc/numpy/>`_
        propose plus de types que Python, les mêmes que le langage C
        (langage de son implémentation). Les programmeurs cherchent toujours
        le plus petit type possible pour représenter un nombre.
        Si une matrice ne possède que des entiers entre 0 et 255,
        on peut utiliser le type *numpy.uint8* qui est codé sur un octet.
        Cela explique pourquoi beaucoup de libraires de machine learning sont codées
        des *numpy.float32*, soit 4 octets plutôt que *numpy.float64* ou *double*.
        Deux raisons à cela, les *numpy.float32* prennent deux fois
        moins de place en mémoire.
        Le coût des calculs avec des *double* est plus coûteux avec les GPU.
        Lire `Explaining FP64 performance on GPUs
        <https://arrayfire.com/blog/explaining-fp64-performance-on-gpus/>`_.
    """

    return [
        numpy.bool_,
        numpy.int_,
        numpy.intc,
        numpy.intp,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float_,
        numpy.float16,
        numpy.float32,
        numpy.float64,
        numpy.complex_,
        numpy.complex64,
        numpy.complex128,
    ]
