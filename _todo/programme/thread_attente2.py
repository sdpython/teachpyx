# coding: latin-1
import threading, time

class MonThread (threading.Thread) :
    def __init__ (self, jusqua, event) :    # event = objet Event
        threading.Thread.__init__ (self)    #       = donnée supplémentaire
        self.jusqua = jusqua                
        self.event  = event                 # on garde un accès à l'objet Event
        
    def run (self) :
        for i in range (0, self.jusqua) :
            print("thread itération ", i)
            time.sleep (0.1)
        self.event.set ()                   # on indique qu'on a fini : 
                                            # on active l'object self.event
print("début")
        
event = threading.Event ()       # on crée un objet de type Event
event.clear ()                   # on désactive l'ojet Event
m = MonThread (10, event)        # crée un thread
m.start ()                       # démarre le thread, 
event.wait ()                    # on attend jusqu'à ce que l'objet soit activé
                                 # event.wait (0.1) : n'attend qu'un
print("fin")                     #          seulement 1 dizième de seconde