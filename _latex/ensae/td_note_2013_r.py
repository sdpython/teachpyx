# coding:utf-8
import re
import sys

sys.path.append("../../complements_site_web")
# import importme


def recupere_donnees():
    """
    0 S�ance
    1 R�f�rence
    2 Entit� d�positaire
    3 Elu d�positaire
    4 Objet
    5 Type
    6 Rapporteur
    """
    file = importme.import_module("td_note_2013_ordre_du_jour_conseil_municipal.zip")[0]
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    lines = [_ for _ in lines if len(_) > 0]
    lines = [_.split("\t") for _ in lines][1:]
    lines = [(_[0], _[4]) for _ in lines if len(_) > 5]
    return lines


def extrait_montant(objet):
    exp = re.compile("[ (]([0-9.,]+) {0,3}euros")
    res = exp.search(objet)
    if res:
        montant = res.groups()[0]
        return montant
    else:
        print("probl�me ", objet)
        return None

    """Subvention � l'Association des Commer�ants de la rue 
    Mesnil (16e) pour les illuminations � l'occasion
    des f�tes de fin d'ann�e 2007, dans le cadre de 
    l'op�ration "Paris Illumine Paris". -
    Montant : 7.000 euros.	
    PJ	Mme Lyne COHEN-SOLAL (2�me Commission) rapporteure."""
