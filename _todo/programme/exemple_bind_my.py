# coding: latin-1
import Tkinter
def affiche_touche_pressee () : root.event_generate ("<<perso>>", rooty = -5)
def perso (evt) : print "perso", evt.y_root
root = Tkinter.Tk ()
b = Tkinter.Button (text = "clic", \
                    command = affiche_touche_pressee)
b.pack ()
root.bind ("<<perso>>", perso)  # on intercepte un événement personnalisé
root.mainloop ()