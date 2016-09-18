# coding: latin-1
import tkinter as Tk
root = Tk.Tk ()

o = Tk.ComboBox (root, label = "label")
o.insert (Tk.END, "ligne 1")
o.insert (Tk.END, "ligne 2")
o.insert (Tk.END, "ligne 3")
o.insert (Tk.END, "ligne 4")
o.pack ()

def print_file () :                     # voir le chapitre sur les événéments
    print (o.cget ("value"))            # idem

b = Tk.Button (root, text = "print")
b.config (command = print_file)         # idem
b.pack ()

root.mainloop ()                        # idem