# coding: utf-8
import urllib
import os
import os.path


def charge_donnees(nom="donnees_enquete_2003_television.txt"):
    if os.path.exists(nom):
        # si le fichier existe (il a d�j� �t� t�l�charg� une fois)
        f = open(nom, "r")
        text = f.read()
        f.close()
    else:
        # si le fichier n'existe pas
        link = "???" + "python_td_minute/data/examen/" + nom
        url = urllib.urlopen(link)
        text = url.read()
        # on enregistre les donn�es pour �viter de les t�l�charger une seconde fois
        f = open(nom, "w")
        f.write(text)
        f.close()

    lines = text.split("\n")
    lines = [li.split("\t") for li in lines if len(li) > 3]
    lines = [["0" if s.strip() == "" else s for s in li] for li in lines]
    return lines
