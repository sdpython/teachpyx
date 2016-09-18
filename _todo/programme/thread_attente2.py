# coding: latin-1
import threading, time

class MonThread (threading.Thread) :
    def __init__ (self, jusqua, event) :    # event = objet Event
        threading.Thread.__init__ (self)    #       = donn�e suppl�mentaire
        self.jusqua = jusqua                
        self.event  = event                 # on garde un acc�s � l'objet Event
        
    def run (self) :
        for i in range (0, self.jusqua) :
            print("thread it�ration ", i)
            time.sleep (0.1)
        self.event.set ()                   # on indique qu'on a fini : 
                                            # on active l'object self.event
print("d�but")
        
event = threading.Event ()       # on cr�e un objet de type Event
event.clear ()                   # on d�sactive l'ojet Event
m = MonThread (10, event)        # cr�e un thread
m.start ()                       # d�marre le thread, 
event.wait ()                    # on attend jusqu'� ce que l'objet soit activ�
                                 # event.wait (0.1) : n'attend qu'un
print("fin")                     #          seulement 1 dizi�me de seconde