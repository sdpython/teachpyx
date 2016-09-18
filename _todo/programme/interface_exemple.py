import Tkinter as T
root = T.Tk ()


l = T.Label (text = "lkfjhsdfkds")
l.pack ()

b = T.Button ()
b.pack ()

e = T.Entry ()
e.pack ()
e.insert (0, "texte")
print "e = ", e.get ()

t = T.Text ()
t.pack ()
t.config (width = 100, height = 10)

i = T.IntVar ()
c = T.Checkbutton (text = "coche", variable = i)
c.pack ()
i.set (1)

j = T.IntVar ()
r1 = T.Radiobutton (text = "option1", variable = j, value = 1)
r2 = T.Radiobutton (text = "option2", variable = j, value = 2)
r3 = T.Radiobutton (text = "option3", variable = j, value = 2)
j.set (2)
r1.pack ()
r2.pack ()
r3.pack ()

l = T.Listbox ()
l.pack (side = T.RIGHT)
l.insert (0, "ligne")
l.insert (1, "colonne")

im = T.PhotoImage (file = "chal_mono.GIF")
b.config (image = im)

def affiche () :
    t.insert ("0.0", "bravo")
    s = t.get ("0.0", "end")
    print s

b.config (command = affiche)

root.mainloop ()