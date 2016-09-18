# coding: latin-1
def import_fichier (module) :
    import os.path
    import sys
    if os.path.exists (module) :           # on teste l'existence du fichier
        folder,name = os.path.split (module)  # on obtient le r�pertoire du module
        if folder not in sys.path :
            sys.path.append (folder)       # on ajoute le r�pertoire dans la liste
                                           # des r�pertoires autoris�s
        name = name.replace (".py", "")    # on enl�ve l'extension
        module = __import__ (name)         # on importe le module
        return module
    else :
        # si le fichier n'existe pas --> on l�ve une exception
        raise ImportError ("impossible d'importer le module " + module)
        
# on importe un module    
mod = import_fichier (r"D:\Dupre\informatique\programme\corde.py")
# on affiche l'aide associ�e
help (mod)