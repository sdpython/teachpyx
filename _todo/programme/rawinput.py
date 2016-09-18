import Tkinter
def question (legende) :
    reponse = [""]
    root = Tkinter.Tk ()
    root.title ("pseudo raw_input")
    Tkinter.Label (text = legende).pack (side = Tkinter.LEFT)
    s = Tkinter.Entry (text= "def", width=80)
    s.pack (side = Tkinter.LEFT)
    def rget () :
        reponse [0] = s.get ()
        root.destroy ()
    Tkinter.Button (text = "ok", command = rget).pack (side = Tkinter.LEFT)
    root.mainloop ()
    return reponse [0]
    
print "reponse ", question ("texte de la question")  