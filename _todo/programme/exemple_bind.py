import tkinter
root = tkinter.Tk()
b = tkinter.Button(text="appuyer sur une touche")
b.pack()

def affiche_touche_pressee (evt) :
    print("--------------------------- touche pressee")
    print("evt.char = ", evt.char)
    print("evt.keysym = ", evt.keysym)
    print("evt.num = ", evt.num)
    print("evt.x,evt.y = ", evt.x, ",", evt.y)
    print("evt.x_root,evt.y_root = ", evt.x_root, ",", evt.y_root)
    print("evt.widget = ", evt.widget)
    
b.bind ("<Key>", affiche_touche_pressee)
b.bind ("<Button-1>", affiche_touche_pressee)
b.bind ("<Motion>", affiche_touche_pressee)
b.focus_set ()

root.mainloop ()