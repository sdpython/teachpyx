import tkinter
root = tkinter.Tk ()
l = tkinter.Label (text = "0 secondes")
l.pack ()
sec = 0
id = None

def change_legende() :
    global l
    global sec
    global id
    sec += 1
    l.config (text = "%d secondes" % sec)
    id = l.after (1000, change_legende)

l.after (1000, change_legende)

root.mainloop ()