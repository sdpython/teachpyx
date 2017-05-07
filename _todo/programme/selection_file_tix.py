import tkinter.tix as tix
root = tix.Tk ()

o = tix.FileSelectBox (root)
o.pack ()

def print_file () :
    print(o.cget ("value"))

b = tix.Button (root, text = "print")
b.config (command = print_file)
b.pack ()

root.mainloop ()