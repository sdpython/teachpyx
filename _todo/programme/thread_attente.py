# coding: latin-1
import threading, time

class MonThread (threading.Thread) :
    def __init__ (self, jusqua) :
        threading.Thread.__init__ (self)
        self.jusqua = jusqua
        self.etat = False       # l'état du thread est soit False (à l'arrêt)
                                # soit True (en marche)
        
    def run (self) :
        self.etat = True                        # on passe en mode marche
        for i in range (0, self.jusqua) :
            print("thread itération ", i)
            time.sleep (0.1)
        self.etat = False                       # on revient en mode arrêt
        
m = MonThread (10)          # crée un thread
m.start ()                  # démarre le thread, 

print("début")

while m.etat == False :
    # on attend que le thread démarre
    time.sleep (0.1)  # voir remarque ci-dessous
    
while m.etat == True :
    # on attend que le thread s'arrête
    # il faut introduire l'instruction time.sleep pour temporiser, il n'est pas 
    # nécessaire de vérifier sans cesse que le thread est toujours en marche
    # il suffit de le vérifier tous les 100 millisecondes
    # dans le cas contraire, la machine passe son temps à vérifier au lieu
    # de se consacrer à l'exécution du thread
    time.sleep (0.1)
    
print("fin")