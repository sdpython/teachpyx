# coding: latin-1
"""ce programme d�termine toutes les fonctions d�finies dans 
un programme et jamais appel�es"""
import glob
import os
import re


def trouve_toute_fonction (s, exp, gr, expm = "^$") :
    """ � partir d'une cha�ne de caract�res correspondant
    � un programme Python, cette fonction retourne 
    une liste de 3-uples, chacun contient :
        - le nom de la fonction
        - (debut,fin) de l'expression dans la cha�ne
        - la ligne o� elle a �t� trouv�e
       
    Param�tres:
       - s    : cha�ne de caract�res
       - exp  : cha�ne de caract�res correspond � l'expression
       - gr   : num�ro de groupe correspondant au nom de la fonction
       - expm : expression n�gative
    """
    exp = re.compile (exp)
    res = []
    pos = 0
    r = exp.search (s, pos)   # premi�re recherche
    while r is not None :
        temp = (r.groups()[gr], r.span(gr), r.group(gr))
        x    = re.compile(expm.replace ("function", temp [0]) )
        if not x.match(temp[2]) :  
            # l'expression n�gative n'est pas trouv�, on peut ajouter ce r�sultat
            res.append(temp)
        r = exp.search(s, r.end(gr))     # recherche suivante
    return res

def get_function_list_definition (s) :
    """trouve toutes les d�finitions de fonctions"""
    return trouve_toute_fonction (s, \
              "\ndef[ ]+([a-zA-Z_][a-zA-Z_0-9]*)[ ]*[(].*[)][ ]*[:]", 0)

def get_function_list_call (s) :
    """trouve tous les appels de fonctions"""
    return trouve_toute_fonction (s, \
              "\n.*[=(,[{ .]([a-zA-Z_][a-zA-Z_0-9]*)(?![ ]?:)[ ]*[(].*[)]?", 0, \
              "^\\n[ ]*(class|def)[ ]+function.*$")
                
def detection_fonction_pas_appelee (file) :                
    """retourne les couples de fonctions jamais appel�es suivies
    du num�ro de la ligne o� elles sont d�finies"""

    f       = open (file, "r")
    li      = f.readlines ()
    f.close ()
    sfile   = "".join (li)
    
    funcdef = get_function_list_definition (sfile)
    funccal = get_function_list_call (sfile)
    f2 = [ p [0] for p in funccal ]
    res = []
    for f in funcdef :
        if f [0] not in f2 : 
            ligne = sfile [:f [1][0]].count ("\n")
            res.append ( (f [0], ligne+2))
    return res
    
def fonction_inutile () :  # ligne 63
    pass

file = __file__
print(detection_fonction_pas_appelee(file))   
            # affiche [('fonction_inutile', 63)]