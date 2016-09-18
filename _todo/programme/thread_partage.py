# coding: latin-1
import threading, time

message = ""
verrou  = threading.Lock ()

def ajoute (c) :
    global message     # message et verrou sont des variables gloables
    global verrou      # pour ne pas qu'elle disparaisse dès la fin de la fonction
    #verrou.acquire ()  # on protège ce qui suit  (*)
    
    s = message + c    # instructions jamais exécutée simultanément par 2 threads
    time.sleep (0.001) # time.sleep : pour exagérer le défaut de synchronisation
    message = s        # si verrou n'est pas utilisé
    
    #verrou.release ()  # on quitte la section protégée  (*)

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
        
print("début")

# synchronisation attente
e1 = threading.Event ()
e2 = threading.Event ()
e1.clear ()
e2.clear ()

m1 = MonThread (10, e1, "1")     # crée un thread
m1.start ()                      # démarre le thread, 
m2 = MonThread (10, e2, "2")     # crée un second thread
m2.start ()                      # démarre le second thread, 

e1.wait ()
e2.wait ()

print("longueur ", len(message)) # affiche 20
print("message = ", message)     # affiche quelque chose comme 12212112211212121221
