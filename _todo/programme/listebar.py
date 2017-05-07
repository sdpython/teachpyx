# -*- coding: utf-8 -*-
import tkinter
import tkinter.scrolledtext
root = tkinter.Tk ()

o = tkinter.scrolledtext.ScrolledText (root)
for k in range (0,100) : 
    o.insert (tkinter.END, "ligne " + str (k))
o.pack ()

def print_file () :                     # voir chapitre sur les événements
    print (o.selection_get ())  # idem 

b = tkinter.Button (root, text = "print")    
b.config (command = print_file)         # idem 
b.pack ()

root.mainloop ()                        # idem 