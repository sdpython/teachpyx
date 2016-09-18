# coding: latin-1
import threading, time

class MonThread (threading.Thread) :
    def __init__ (self, jusqua) :
        threading.Thread.__init__ (self)
        self.jusqua = jusqua
        self.etat = False       # l'�tat du thread est soit False (� l'arr�t)
                                # soit True (en marche)
        
    def run (self) :
        self.etat = True                        # on passe en mode marche
        for i in range (0, self.jusqua) :
            print("thread it�ration ", i)
            time.sleep (0.1)
        self.etat = False                       # on revient en mode arr�t
        
m = MonThread (10)          # cr�e un thread
m.start ()                  # d�marre le thread, 

print("d�but")

while m.etat == False :
    # on attend que le thread d�marre
    time.sleep (0.1)  # voir remarque ci-dessous
    
while m.etat == True :
    # on attend que le thread s'arr�te
    # il faut introduire l'instruction time.sleep pour temporiser, il n'est pas 
    # n�cessaire de v�rifier sans cesse que le thread est toujours en marche
    # il suffit de le v�rifier tous les 100 millisecondes
    # dans le cas contraire, la machine passe son temps � v�rifier au lieu
    # de se consacrer � l'ex�cution du thread
    time.sleep (0.1)
    
print("fin")