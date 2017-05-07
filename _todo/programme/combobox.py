# -*- coding: utf-8 -*-
import tkinter
import tkinter.ttk as ttk

root = tkinter.Tk()

o = ttk.Combobox(root, values=["ligne 1", "ligne 2", "ligne 3", "ligne 4"])
o.pack ()

def print_file () :                     # voir le chapitre sur les événements
    print(o.get())

b = tkinter.Button (root, text="print")
b.config (command = print_file)         # idem
b.pack ()

help(tkinter.Button.__init__)

root.mainloop()                         # idem
