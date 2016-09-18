import tkinter as Tkinter
root = Tkinter.Tk ()

e = Tkinter.Text (width = 50, height = 10)
e.pack ()

m = Tkinter.Menu ()

sm1 = Tkinter.Menu ()
sm2 = Tkinter.Menu ()

m.add_cascade (label = "sous-menu 1", menu = sm1)
m.add_cascade (label = "sous-menu 2", menu = sm2)

nb = 0

def affiche () : print ("fonction affiche")
def calcul () : print ("fonction calcul ", 3 * 4)
def ajoute_bouton () :
    global nb
    nb += 1
    b = Tkinter.Button (text = "bouton " + str (nb))
    b.pack ()

sm1.add_command (label = "affiche",       command = affiche)
sm1.add_command (label = "calcul",        command = calcul)
sm2.add_command (label = "ajoute_bouton", command = ajoute_bouton)
sm2.add_command (label = "fin",           command = root.destroy)

root.config (menu = m, width = 200)
root.title ("essai de menu")
#help (Tkinter.Tk)
root.mainloop ()