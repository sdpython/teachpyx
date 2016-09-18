# coding: latin-1
# la première ligne autorise les accents
import Tkinter
root = Tkinter.Tk ()
b = Tkinter.Button (text = "fonction change_legende")
b.pack ()

def change_legende () :
    global b
    b.config (text = "nouvelle légende")

b.config (command = change_legende)
root.mainloop ()