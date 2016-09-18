# coding: latin-1
import tkinter as Tk
root = Tk.Tk ()

o = Tk.ScrolledListBox (root)
for k in range (0,100) : o.listbox.insert (Tk.END, "ligne " + str (k))
o.pack ()

def print_file () :                     # voir chapitre sur les événements
    print (o.listbox.selection_get ())  # idem 

b = Tk.Button (root, text = "print")    
b.config (command = print_file)         # idem 
b.pack ()

root.mainloop ()                        # idem 