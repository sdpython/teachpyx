# coding: latin-1
def addition (l1, l2):
    """cette fonction additionne deux listes
    >>> addition ( [], [])
    []
    >>> addition ( [1,2], [3,-1])
    [4, 1]
    >>> addition ( [1], [3,-1])
    Traceback (most recent call last):
        ...
    Exception: listes de tailles différentes
    """
    if len (l1) != len (l2) :
        raise Exception ("listes de tailles différentes")
    res = []
    for i in range (0, len (l1)) :
        res.append ( l1 [i] + l2 [i] )
    return res

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()