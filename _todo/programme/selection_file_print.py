# coding: latin-1
"""module permettant de sélection un fichier,
fonctionne sans interface graphique"""
import os.path
import os

class FileSelection (object) :
    """classe permettant de sélectionner un fichier 
    sans boîte de dialogue"""
    
    def __init__ (self, titre = "Sélection de fichier", \
                    chemin = None, file = True, exist= True) :
        """initialise la classe
        @param      titre           titre de la fenêtre
        @param      chemin          fichier ou répertoire par défaut
        @param      file            True : fichier, False : répertoire
        @param      exist           True : le répertoire ou le fichier 
                                           sélectionné doit exister"""
        self.titre  = titre
        self.chemin = chemin
        self.file   = file
        self.exist  = exist
        
        if self.chemin == None :  self.chemin = os.getcwd ()
            
    def get_list (self) :
        """retourne la liste des fichiers et des répertoires (2 listes), 
        répertoires seulement et [] si self.file == False"""
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
        """lance la sélection d'un fichier"""

        def update_chemin () :
            """mise à jour du chemin dans la boîte de dialogue"""
            pass

        def update_list () :
            """mise à jour de la liste des fichiers et répertoires 
            à partir de la chaîne dans la boîte de dialogue"""
            lidir, lifile   = self.get_list ()
            print "  répertoires"
            for l in lidir : print "      ", l
            print "  fichiers"
            for l in lifile : print "      ", l
                    
        def precedent () :
            """passe au répertoire précédent"""
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
            """rentre dans un répertoire"""
            sel2 = self.chemin + "\\" + sel
            if os.path.isdir (sel2) :
                self.chemin = sel2
                #update_chemin ()
                #update_list ()
            
        def update_sel () :
            """mise à jour de la chaîne de caractères 
            dans la boîte de dialogue à partir de la ligne
            sélectionnée dans la liste"""
            pass
                
        def annuler () :
            """annule la recherche"""
            self.resultat = False
        
        def accepter () :
            """accepte le résultat"""
            self.resultat = True

        while True :
            print "chemin actuel : ", self.chemin
            print "liste des fichiers et répertoire inclus"
            update_list ()
            print "quelle action : Précédent, Entre, Annuler, " \
                   "Ok (entrer la lettre majuscule)\n"
            str = raw_input ("")
            if str == "P" :
                precedent ()
            elif str == "E" :
                sel = raw_input ("entrer un nom de répertoire\n")
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
                print "choix incompréhensible"
            print "--------------------------------------------"
            
        if self.resultat : return self.chemin
        else : return None
            
            
if __name__ == "__main__" :
    r = FileSelection ("sélection d'un fichier", "c:\\")
    s = r.run ()
    print "fichier sélectionné ", s
       
    