# coding: latin-1
"""genhelp.py : g�n�ration automatique de l'aide dans le r�pertoire d'ex�cution"""
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
        """unique m�thode"""
        return 1

def generate_help_file (f, pyt = python_path, pyd = pydoc_path) :
    """g�n�re l'aide associ�e � un fichier ou un module
    le nom de ce fichier peut appara�tre sans son extension ou alors
    pr�c�d� de .\\ ou avec son chemin complet
    pyt est le r�pertoire de python
    pyd est l'emplacement de pydoc.py"""
    s = "call " + pyt + " " + pyd + " -w " + f
    os.system (s)
    
def replace_firstpage (file, page) :
    """la g�n�ration de l'aide chm s'arr�te avant la fin si le lien <a href=".">index</a>
    est laiss� dans les pages g�n�r�es par pydoc, on le remplace par une page
    comme index.html"""
    f = open (file, "r")
    li = f.readlines ()
    f.close ()
    f = open (file, "w")
    for l in li :
        f.write (l.replace ("""<a href=".">index</a>""", page))
    f.close ()
    
def genhelp (files, pyt = python_path, pyd = pydoc_path, firstpage = "index.html") :
    """g�n�re l'aide associ�e � des fichiers ou des modules,
    un fichier se distingue d'un module par son extension,
    retourne la liste des fichiers g�n�r�s,
    pyt est le r�pertoire de python
    pyd est l'emplacement de pydoc.py
    firstpage voir fonction replace_firstpage"""
    res = []
    for f in files :
        print "g�n�ration de l'aide de ", f
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