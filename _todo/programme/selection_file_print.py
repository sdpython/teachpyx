# coding: latin-1
"""module permettant de s�lection un fichier,
fonctionne sans interface graphique"""
import os.path
import os

class FileSelection (object) :
    """classe permettant de s�lectionner un fichier 
    sans bo�te de dialogue"""
    
    def __init__ (self, titre = "S�lection de fichier", \
                    chemin = None, file = True, exist= True) :
        """initialise la classe
        @param      titre           titre de la fen�tre
        @param      chemin          fichier ou r�pertoire par d�faut
        @param      file            True : fichier, False : r�pertoire
        @param      exist           True : le r�pertoire ou le fichier 
                                           s�lectionn� doit exister"""
        self.titre  = titre
        self.chemin = chemin
        self.file   = file
        self.exist  = exist
        
        if self.chemin == None :  self.chemin = os.getcwd ()
            
    def get_list (self) :
        """retourne la liste des fichiers et des r�pertoires (2 listes), 
        r�pertoires seulement et [] si self.file == False"""
        if os.path.isdir (self.chemin) :
            list    = os.listdir (self.chemin)
        else : 
            ch,fi   = os.path.split (self.chemin)
            list    = os.listdir (ch)
        
        lifile  = []
        lidir   = []
        for l in list :
            if os.path.isdir (self.chemin + "\\" + l) : 
                lidir.append (l)
            elif self.file : 
                lifile.append (l)
                
        lidir.sort ()
        lifile.sort ()
        return lidir, lifile
        
    def run (self) :
        """lance la s�lection d'un fichier"""

        def update_chemin () :
            """mise � jour du chemin dans la bo�te de dialogue"""
            pass

        def update_list () :
            """mise � jour de la liste des fichiers et r�pertoires 
            � partir de la cha�ne dans la bo�te de dialogue"""
            lidir, lifile   = self.get_list ()
            print "  r�pertoires"
            for l in lidir : print "      ", l
            print "  fichiers"
            for l in lifile : print "      ", l
                    
        def precedent () :
            """passe au r�pertoire pr�c�dent"""
            if os.path.isdir (self.chemin) :
                ch, last    = os.path.split (self.chemin)
                self.chemin = ch
            else :
                ch, last    = os.path.split (self.chemin)
                ch, last    = os.path.split (ch)
                self.chemin = ch
            #update_chemin ()
            #update_list ()
        
        def suivant (sel) :
            """rentre dans un r�pertoire"""
            sel2 = self.chemin + "\\" + sel
            if os.path.isdir (sel2) :
                self.chemin = sel2
                #update_chemin ()
                #update_list ()
            
        def update_sel () :
            """mise � jour de la cha�ne de caract�res 
            dans la bo�te de dialogue � partir de la ligne
            s�lectionn�e dans la liste"""
            pass
                
        def annuler () :
            """annule la recherche"""
            self.resultat = False
        
        def accepter () :
            """accepte le r�sultat"""
            self.resultat = True

        while True :
            print "chemin actuel : ", self.chemin
            print "liste des fichiers et r�pertoire inclus"
            update_list ()
            print "quelle action : Pr�c�dent, Entre, Annuler, " \
                   "Ok (entrer la lettre majuscule)\n"
            str = raw_input ("")
            if str == "P" :
                precedent ()
            elif str == "E" :
                sel = raw_input ("entrer un nom de r�pertoire\n")
                suivant (sel)
            elif str == "A" : 
                annuler ()
                break   # on sort de la boucle
            elif str == "O" : 
                print "Entrer un nom de fichier"
                str = raw_input ("\n")
                self.chemin += "\\" + str
                accepter ()
                break   # on sort de la boucle
            else :
                print "choix incompr�hensible"
            print "--------------------------------------------"
            
        if self.resultat : return self.chemin
        else : return None
            
            
if __name__ == "__main__" :
    r = FileSelection ("s�lection d'un fichier", "c:\\")
    s = r.run ()
    print "fichier s�lectionn� ", s
       
    