# coding: cp1252
import threading, time

class MonThread (threading.Thread) :
    def __init__ (self, jusqua) :      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)# ne pas oublier cette ligne 
                                       # (appel au constructeur de la classe mère)
        self.jusqua = jusqua           # donnée supplémentaire ajoutée à la classe
        
    def run (self) :
        for i in range (0, self.jusqua) :
            print("thread ", i)
            time.sleep (0.08)    # attend 100 millisecondes sans rien faire
                                # facilite la lecture de l'affichage
        
m = MonThread (10)          # crée le thread
m.start ()                  # démarre le thread, 
                            # l'instruction est exécutée en quelques millisecondes
                            # quelque soit la durée du thread

for i in range (0,10) :
    print("programme ", i)
    time.sleep (0.1)            # attend 100 millisecondes sans rien faire
                                # facilite la lecture de l'affichage