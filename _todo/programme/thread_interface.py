# coding: latin-1
import threading, time, random, copy

# d�finition du thread
class MonThread (threading.Thread) :
    def __init__ (self, win, res) :
        threading.Thread.__init__ (self)
        self.win = win  # on m�morise une r�f�rence sur la fen�tre
        self.res = res
        
    def run (self) :
        for i in range (0, 10) :
            print("thread ", i)
            time.sleep (0.1)
            
          # afin que le thread retourne un r�sultat
          # self.res d�signe thread_resultat qui re�oit un nombre de plus
        h = random.randint (0,100)
        self.res.append (h)    
        
          # on lance un �v�nement <<thread_fini>> � la fen�tre principale 
          # pour lui dire que le thread est fini, l'�v�nement est ensuite 
          # g�r� par la boucle principale de messages
          # on peut transmettre �galement le r�sultat lors de l'envoi du message
          # en utilisant un attribut de la classe Event pour son propre compte
        self.win.event_generate ("<<thread_fini>>", x = h)
    
thread_resultat = []

def lance_thread () :
    global thread_resultat
      # fonction appel�e lors de la pression du bouton
      # on change la l�gnde de la zone de texte
    text .config (text = "thread d�marr�")
    text2.config (text = "thread d�marr�")
      # on d�sactive le bouton pour �viter de lancer deux threads en m�me temps
    bouton.config (state = TK.DISABLED)
      # on lance le thread
    m = MonThread (root, thread_resultat)
    m.start ()
    
def thread_fini_fonction (e) :
    global thread_resultat
      # fonction appel�e lorsque le thread est fini
    print("la fen�tre sait que le thread est fini")
      # on change la l�gende de la zone de texte
    text .config (text = "thread fini + r�sultat " + str (thread_resultat))
    text2.config (text = "thread fini + r�sultat (e.x) " + str (e.x))
      # on r�active le bouton de fa�on � pouvoir lancer un autre thread
    bouton.config (state = TK.NORMAL)

import tkinter as TK

# on cr�e la fen�tre
root   = TK.Tk ()
bouton = TK.Button (root, text = "thread d�part", command = lance_thread)
text   = TK.Label (root, text = "rien")
text2  = TK.Label (root, text = "rien")
bouton.pack ()
text.pack ()
text2.pack ()

# on associe une fonction � un �v�nement <<thread_fini>> propre au programme
root.bind ("<<thread_fini>>", thread_fini_fonction)

# on active la boucle principale de message
root.mainloop ()