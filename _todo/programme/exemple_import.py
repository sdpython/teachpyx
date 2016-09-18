# coding: latin-1
def import_fichier (module) :
    import os.path
    import sys
    if os.path.exists (module) :           # on teste l'existence du fichier
        folder,name = os.path.split (module)  # on obtient le répertoire du module
        if folder not in sys.path :
            sys.path.append (folder)       # on ajoute le répertoire dans la liste
                                           # des répertoires autorisés
        name = name.replace (".py", "")    # on enlève l'extension
        module = __import__ (name)         # on importe le module
        return module
    else :
        # si le fichier n'existe pas --> on lève une exception
        raise ImportError ("impossible d'importer le module " + module)
        
# on importe un module    
mod = import_fichier (r"D:\Dupre\informatique\programme\corde.py")
# on affiche l'aide associée
help (mod)