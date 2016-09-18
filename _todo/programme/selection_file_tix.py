import Tix as Tk
root = Tk.Tk ()

o = Tk.FileSelectBox (root)
o.pack ()

def print_file () :
    print o.cget ("value")

b = Tk.Button (root, text = "print")
b.config (command = print_file)
b.pack ()

root.mainloop ()