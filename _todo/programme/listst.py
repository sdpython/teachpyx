# -*- coding: utf-8 -*-
import tkinter

class MaListbox(tkinter.Listbox):
    def __init__(self, master = None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        tkinter.Listbox.__init__(self, master, cnf, **kw)  
        self.bind("<Motion>", self.mouvement)
        self.pos = None  # mémoire l'ancienne position du curseur
    def mouvement(self, ev):
        pos = self.nearest(ev.y)  # nouvelle position du curseur
        if pos < 0 or pos >= self.size(): return
        if self.pos != pos:
            if self.pos != None: self.itemconfig(self.pos, bg='')
            self.itemconfigure(pos, bg='gray')
            self.pos = pos

root = tkinter.Tk()
b = MaListbox()
b.insert("end", "ligne 1")
b.insert("end", "ligne 2")
b.insert("end", "ligne 3")
b.pack()
b.focus_set()
root.mainloop()