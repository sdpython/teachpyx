# coding: latin-1
import Tkinter as Tk

class MaFenetreSeq :
    def __init__ (self, win) :
        self.win = win
        self.creation ()
        self.sequence = []
        
    def creation (self) :
        b1 = Tk.Button (self.win, text="bouton 1", command=self.commande_bouton1)
        b2 = Tk.Button (self.win, text="bouton 2", command=self.commande_bouton2)
        b3 = Tk.Button (self.win, text="remise à zéro", command=self.zero)
        b1.grid (row=0, column=0)
        b2.grid (row=0, column=1)
        b3.grid (row=0, column=2)
        self.lab = Tk.Label (self.win, text = "-")
        
    def commande_bouton1 (self) :
        # ajoute 1 à la liste self.sequence
        self.sequence.append (1)
        self.controle ()
        
    def commande_bouton2 (self) :
        # ajoute 2 à la liste self.sequence
        self.sequence.append (2)
        self.controle ()
        
    def zero (self) :
        # on vide la liste self.sequence
        self.sequence = []
        self.lab.grid_forget ()
        
    def controle (self) :
        # on compare la liste sequence à [1,2,1] et [2,2,1,1]
        # dans ce cas, on fait apparaître l'objet lab
        l = len (self.sequence)
        if l >= 3 and self.sequence [l-3:] == [1,2,1] :
            self.lab.configure (text = "séquence 1 2 1")
            self.lab.grid (row = 1, column = 0)
        elif l >= 4 and self.sequence [l-4:] == [2,2,1,1] :
            self.lab.configure (text = "séquence 2 2 1 1")
            self.lab.grid (row = 1, column = 1)
    
if __name__ == "__main__" :
    root = Tk.Tk ()
    f = MaFenetreSeq (root)
    root.mainloop ()