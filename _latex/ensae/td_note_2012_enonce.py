# coding: utf-8
import urllib
import os
import os.path


def charge_donnees(nom="donnees_enquete_2003_television.txt"):
    if os.path.exists(nom):
        # si le fichier existe (il a déjà été téléchargé une fois)
        with open(nom, "r") as f:
            text = f.read()
    else:
        # si le fichier n'existe pas
        link = "???" + "python_td_minute/data/examen/" + nom
        url = urllib.urlopen(link)
        text = url.read()
        # on enregistre les données pour éviter de les télécharger une seconde fois
        with open(nom, "w") as f:
            f.write(text)

    lines = text.split("\n")
    lines = [li.split("\t") for li in lines if len(li) > 3]
    lines = [["0" if s.strip() == "" else s for s in li] for li in lines]
    return lines
