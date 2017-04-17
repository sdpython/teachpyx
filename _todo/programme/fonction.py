# coding: latin-1
"""ce programme détermine toutes les fonctions définies dans 
un programme et jamais appelées"""
import glob
import os
import re


def trouve_toute_fonction (s, exp, gr, expm = "^$") :
    """ à partir d'une chaîne de caractères correspondant
    à un programme Python, cette fonction retourne 
    une liste de 3-uples, chacun contient :
        - le nom de la fonction
        - (debut,fin) de l'expression dans la chaîne
        - la ligne où elle a été trouvée
       
    Paramètres:
       - s    : chaîne de caractères
       - exp  : chaîne de caractères correspond à l'expression
       - gr   : numéro de groupe correspondant au nom de la fonction
       - expm : expression négative
    """
    exp = re.compile (exp)
    res = []
    pos = 0
    r = exp.search (s, pos)   # première recherche
    while r is not None :
        temp = (r.groups()[gr], r.span(gr), r.group(gr))
        x    = re.compile(expm.replace ("function", temp [0]) )
        if not x.match(temp[2]) :  
            # l'expression négative n'est pas trouvé, on peut ajouter ce résultat
            res.append(temp)
        r = exp.search(s, r.end(gr))     # recherche suivante
    return res

def get_function_list_definition (s) :
    """trouve toutes les définitions de fonctions"""
    return trouve_toute_fonction (s, \
              "\ndef[ ]+([a-zA-Z_][a-zA-Z_0-9]*)[ ]*[(].*[)][ ]*[:]", 0)

def get_function_list_call (s) :
    """trouve tous les appels de fonctions"""
    return trouve_toute_fonction (s, \
              "\n.*[=(,[{ .]([a-zA-Z_][a-zA-Z_0-9]*)(?![ ]?:)[ ]*[(].*[)]?", 0, \
              "^\\n[ ]*(class|def)[ ]+function.*$")
                
def detection_fonction_pas_appelee (file) :                
    """retourne les couples de fonctions jamais appelées suivies
    du numéro de la ligne où elles sont définies"""

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