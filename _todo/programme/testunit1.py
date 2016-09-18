# coding: latin-1
def addition (l1, l2):
    """cette fonction additionne deux listes"""
    if len (l1) != len (l2) :
        raise Exception ("listes de tailles différentes")    
    res = []
    for i in range (0, len (l1)) :
        res.append ( l1 [i] + l2 [i] )
    return res