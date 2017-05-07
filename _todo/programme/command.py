# -*- coding: utf-8 -*-
# la première ligne autorise les accents
import tkinter
root = tkinter.Tk ()
b = tkinter.Button (text = "fonction change_legende")
b.pack ()

def change_legende () :
    global b
    b.config (text = "nouvelle légende")

b.config (command = change_legende)
root.mainloop ()
