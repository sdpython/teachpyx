# coding: latin-1
import glob
import os.path

def liste_fichier_repertoire (folder, filter) :
    # résultats
    file,fold = [], []
    
    # recherche des fichiers obéissant au filtre
    res = glob.glob (folder + "\\" + filter)
    
    # on inclut les sous-répertoires qui n'auraient pas été
    # sélectionnés par le filtre
    rep = glob.glob (folder + "\\*")
    for r in rep : 
        if r not in res and os.path.isdir (r) : 
            res.append (r)
            
    # on ajoute fichiers et répertoires aux résultats
    for r in res :
        path = r
        if os.path.isfile (path) :
            # un fichier, rien à faire à part l'ajouter
            file.append (path)
        else :
            # sous-répertoire : on appelle à nouveau la fonction
            # pour retourner la liste des fichiers inclus 
            fold.append (path)
            fi,fo = liste_fichier_repertoire (path, filter)
            file.extend (fi)  # on étend la liste des fichiers
            fold.extend (fo)  # on étend la liste des répertoires 
    # fin
    return file,fold
    
folder = r"."
filter = "*.rst"
file,fold = liste_fichier_repertoire (folder, filter)

for f in file :
    print("fichier ", f)
for f in fold :
    print("répertoire ", f)