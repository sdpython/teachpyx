# coding: latin-1
import Tkinter

class nouvelle_fenetre :
    resultat = []
    def top (self) :
        sec = Tkinter.Toplevel ()
        Tkinter.Label (sec, text="entrer quelque chose").pack ()
        saisie = Tkinter.Entry (sec)
        saisie.pack()
        Tkinter.Button (sec, text = "valider", command = sec.quit).pack ()
        sec.mainloop ()
        nouvelle_fenetre.resultat.append ( saisie.get () )
        sec.destroy ()

root = Tkinter.Tk() #fenetre principale
a = Tkinter.Button (text    = "fenêtre Toplevel", 
                    command = nouvelle_fenetre ().top)
a.pack()
root.mainloop()

for a in nouvelle_fenetre.resultat :
    print "contenu ", a