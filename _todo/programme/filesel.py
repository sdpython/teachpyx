import Tix as Tk
root = Tk.Tk ()

def command_print () : print box.cget("value")

box = Tk.FileSelectBox (root)
box.config (directory="c:\\")
box.pack ()
Tk.Button (root, text = "print", command = command_print).pack ()

root.mainloop ()