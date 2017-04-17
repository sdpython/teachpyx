# coding: latin-1
import glob
import os.path

def liste_fichier_repertoire (folder, filter) :
    # r�sultats
    file,fold = [], []
    
    # recherche des fichiers ob�issant au filtre
    res = glob.glob (folder + "\\" + filter)
    
    # on inclut les sous-r�pertoires qui n'auraient pas �t�
    # s�lectionn�s par le filtre
    rep = glob.glob (folder + "\\*")
    for r in rep : 
        if r not in res and os.path.isdir (r) : 
            res.append (r)
            
    # on ajoute fichiers et r�pertoires aux r�sultats
    for r in res :
        path = r
        if os.path.isfile (path) :
            # un fichier, rien � faire � part l'ajouter
            file.append (path)
        else :
            # sous-r�pertoire : on appelle � nouveau la fonction
            # pour retourner la liste des fichiers inclus 
            fold.append (path)
            fi,fo = liste_fichier_repertoire (path, filter)
            file.extend (fi)  # on �tend la liste des fichiers
            fold.extend (fo)  # on �tend la liste des r�pertoires 
    # fin
    return file,fold
    
folder = r"."
filter = "*.rst"
file,fold = liste_fichier_repertoire (folder, filter)

for f in file :
    print("fichier ", f)
for f in fold :
    print("r�pertoire ", f)