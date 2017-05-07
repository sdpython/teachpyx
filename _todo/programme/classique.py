# -*- coding: utf-8 -*-
import tkinter

class MaFenetre :
    def __init__(self, win) :
        self.win = win
        self.creation()
        
    def creation(self) :
        b1 = tkinter.Button(self.win, text="bouton 1", command=self.commande_bouton1)
        b2 = tkinter.Button(self.win, text="bouton 2", command=self.commande_bouton2)
        b3 = tkinter.Button(self.win, text="disparition", command=self.disparition)
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        self.lab = tkinter.Label(self.win, text = "-")
        
    def commande_bouton1(self) :
        # on déplace l'objet lab de type Label
        self.lab.configure(text = "bouton 1 appuyé")
        self.lab.grid(row = 1, column = 0)
        
    def commande_bouton2(self) :
        # on déplace l'objet lab de type Label
        self.lab.configure(text = "bouton 2 appuyé")
        self.lab.grid(row = 1, column = 1)
        
    def disparition(self) :
        # on fait disparaître l'objet lab de type Label
        self.lab.grid_forget()
    
if __name__ == "__main__" :
    root = tkinter.Tk()
    f = MaFenetre(root)
    root.mainloop()
