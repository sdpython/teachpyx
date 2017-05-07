import tkinter
import tkinter.ttk
import tkinter.tix
root = tkinter.Tk ()

help(tkinter.tix)

e = tkinter.Text (width = 50, height = 10)
e.pack ()

m = tkinter.Menu (root)

sm1 = tkinter.Menu (root)
sm2 = tkinter.Menu (root)

m.add_cascade (label = "sous-menu 1", menu = sm1)
m.add_cascade (label = "sous-menu 2", menu = sm2)

nb = 0

def affiche():
    print ("fonction affiche")
    
def calcul():
    print ("fonction calcul ", 3 * 4)

def ajoute_bouton () :
    global nb
    nb += 1
    b = tkinter.Button (text = "bouton " + str (nb))
    b.pack ()

sm1.add_command (label = "affiche",       command = affiche)
sm1.add_command (label = "calcul",        command = calcul)
sm2.add_command (label = "ajoute_bouton", command = ajoute_bouton)
sm2.add_command (label = "fin",           command = root.destroy)

root.config (menu = m, width = 200)
root.title ("essai de menu")
root.mainloop ()