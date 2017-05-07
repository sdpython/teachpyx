# -*- coding: utf-8 -*-
import tkinter

class nouvelle_fenetre :
    resultat = []
    def top (self) :
        sec = tkinter.Toplevel ()
        tkinter.Label (sec, text="entrer quelque chose").pack ()
        saisie = tkinter.Entry (sec)
        saisie.pack()
        tkinter.Button (sec, text = "valider", command = sec.quit).pack ()
        sec.mainloop ()
        nouvelle_fenetre.resultat.append ( saisie.get () )
        sec.destroy ()

root = tkinter.Tk() #fenetre principale
a = tkinter.Button (text    = "fenêtre Toplevel", 
                    command = nouvelle_fenetre ().top)
a.pack()
root.mainloop()

for a in nouvelle_fenetre.resultat :
    print("contenu ", a)