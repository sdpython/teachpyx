# coding: latin-1
"""genhelp.py : génération automatique de l'aide dans le répertoire d'exécution"""
import os
import sys
python_path = r"c:\python25\python"          # constante
pydoc_path  = r"c:\python25\lib\pydoc.py"    # constante

class ClassExemple :
    """classe vide, exemple d'aide"""
    def __init__ (self) :
        """constructeur"""
        pass
    def methode (self) :
        """unique méthode"""
        return 1

def generate_help_file (f, pyt = python_path, pyd = pydoc_path) :
    """génère l'aide associée à un fichier ou un module
    le nom de ce fichier peut apparaître sans son extension ou alors
    précédé de .\\ ou avec son chemin complet
    pyt est le répertoire de python
    pyd est l'emplacement de pydoc.py"""
    s = "call " + pyt + " " + pyd + " -w " + f
    os.system (s)
    
def replace_firstpage (file, page) :
    """la génération de l'aide chm s'arrête avant la fin si le lien <a href=".">index</a>
    est laissé dans les pages générées par pydoc, on le remplace par une page
    comme index.html"""
    f = open (file, "r")
    li = f.readlines ()
    f.close ()
    f = open (file, "w")
    for l in li :
        f.write (l.replace ("""<a href=".">index</a>""", page))
    f.close ()
    
def genhelp (files, pyt = python_path, pyd = pydoc_path, firstpage = "index.html") :
    """génère l'aide associée à des fichiers ou des modules,
    un fichier se distingue d'un module par son extension,
    retourne la liste des fichiers générés,
    pyt est le répertoire de python
    pyd est l'emplacement de pydoc.py
    firstpage voir fonction replace_firstpage"""
    res = []
    for f in files :
        print "génération de l'aide de ", f
        if ".py" in f : # fichier
            generate_help_file (f, pyt, pyd)
            g    = f.split ("\\")  # ne garde que le nom de fichier et non son chemin
            page = g [ len (g)-1].replace (".py", ".html")
        else :          # module
            generate_help_file (f, pyt, pyd)
            page = f + ".html"
        res.append (page)
        replace_firstpage (page, firstpage)
    return res

if __name__ == "__main__" :
    import sys
    import os

    files = [".\\genchm.py", ".\\genhelp.py", "os", "sys"]
    res   = genhelp (files)
    print res  # ['genchm.html', 'genhelp.html', 'os.html', 'sys.html']