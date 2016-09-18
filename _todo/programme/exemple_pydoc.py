# coding: latin-1
"""aide associ�e � ce module, exemple d'utiliation de pydoc"""
import os.path
import os

def pydoc_present () :
    """teste la pr�sence du fichier pydoc.py"""
    p = "c:\\python26\\lib\\pydoc.py"""
    return os.path.exists (p)
    
def pydoc_generation (file) :
    """g�n�re la documentation associ�e au fichier file"""
    if not pydoc_present () :
        raise Exception ("pydoc n'est pas install�")
    os.system ("c:\\python26\\python c:\\python26\\lib\\pydoc.py -w " + file)

class ExempleClass (object) :
    """exemple de classe avec de la documentation
    la classe contient comme attribut :
       - li : liste quelconque
    """
    def __init__ (self) :
        object.__init__ (self)
        self.li = ["un", "deux"]
    def __str__ (self) :
        """permet d'afficher la classe sous forme de cha�nes de caract�res"""
        return "li = " + str (self.li)
        
if __name__ == "__main__" :
    e = ExempleClass ()
    print e  # affiche li = ['un', 'deux']
    pydoc_generation ("exemple_pydoc")