# coding: latin-1
import threading, time

message = ""
verrou  = threading.Lock ()

def ajoute (c) :
    global message     # message et verrou sont des variables gloables
    global verrou      # pour ne pas qu'elle disparaisse d�s la fin de la fonction
    #verrou.acquire ()  # on prot�ge ce qui suit  (*)
    
    s = message + c    # instructions jamais ex�cut�e simultan�ment par 2 threads
    time.sleep (0.001) # time.sleep : pour exag�rer le d�faut de synchronisation
    message = s        # si verrou n'est pas utilis�
    
    #verrou.release ()  # on quitte la section prot�g�e  (*)

class MonThread (threading.Thread) :
    def __init__ (self, jusqua, event, s) :
        threading.Thread.__init__ (self)
        self.jusqua = jusqua 
        self.s      = s
        self.event  = event
        
    def run (self) :
        for i in range (0, self.jusqua) :
            ajoute (self.s)
        self.event.set ()
        
print("d�but")

# synchronisation attente
e1 = threading.Event ()
e2 = threading.Event ()
e1.clear ()
e2.clear ()

m1 = MonThread (10, e1, "1")     # cr�e un thread
m1.start ()                      # d�marre le thread, 
m2 = MonThread (10, e2, "2")     # cr�e un second thread
m2.start ()                      # d�marre le second thread, 

e1.wait ()
e2.wait ()

print("longueur ", len(message)) # affiche 20
print("message = ", message)     # affiche quelque chose comme 12212112211212121221
