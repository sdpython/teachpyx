# coding: latin-1
def ajoute_resultat_division (nom, x, y) :
    """ajoute le résultat de la division x/y au fichier nom"""
    f = open (nom, "a")
    f.write (str (x) + "/" + str (y) + "= ")
    f.write ( str ((float (x)/y)) + "\n" )     # exception si y == 0
    f.close ()
    
for i in range (0, 5) :
    try :
        print str (i-1) + "/" + str (i-2)
        ajoute_resultat_division ("essai.txt", i-1,i-2)
    except Exception, e : print "erreur avec i = ", i, ",", e