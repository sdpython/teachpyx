# coding: latin-1
import threading, time, queue, random

class Joueur (threading.Thread) :
    
    # initialisation
    def __init__ (self, nom, e, nb = 1000, temps = 0.1) :
        threading.Thread.__init__(self)
        self.nb    = nb
        self.queue = queue.Queue ()
        self.nom   = nom
        self.event = e
        self.temps = temps  # temps de r�flexion
    def Joueur (self, autre_joueur) : self.autre = autre_joueur
        
    # m�thodes : l'adversaire m'envoie un message
    def Joue    (self, nombre) : self.queue.put_nowait ( ("essai", nombre) )
    def Dessus  (self, nombre) : self.queue.put_nowait ( ("dessus", nombre) )
    def Dessous (self, nombre) : self.queue.put_nowait ( ("dessous", nombre) )
    def Gagne   (self, nombre) : 
        while not self.queue.empty () :
            try :self.queue.get ()
            except : pass
        self.queue.put ( ("gagne", nombre) )
              
    # je joue
    def run (self) :
        x = random.randint (0,self.nb)
        print(self.nom, " : je joue (", x, ")")
        i = 0
        a = 0
        b = self.nb
        while True :
            time.sleep (self.temps)
            
            try : 
                m,n = self.queue.get_nowait ()       # d�synchronis�
                #m,n = self.queue.get (timeout = 0.5)# l'un apr�s l'autre
            except queue.Empty: 
                m,n = None,None
                
            # traitement du message --> r�ponse � l'adversaire
            if m == "essai" :
                if n == x : 
                    self.autre.Gagne (n)
                    print(self.nom, " : j'ai perdu apr�s ", i, " essais")
                    break
                elif n < x : self.autre.Dessus  (n)
                else       : self.autre.Dessous (n)
            elif m == "dessus" :  
                a = max (a, n+1)
                continue  # assure l'�quit� en mode l'un apr�s l'autre
            elif m == "dessous" : 
                b = min (b, n-1)
                continue  # assure l'�quit� en mode l'un apr�s l'autre
            elif m == "gagne" :
                print(self.nom, " : j'ai gagn� en ", i, " essais, solution ", n)
                break

            # on fait une tentative
            if a == b : n = a
            else : n = random.randint (a,b)
            self.autre.Joue (n)
            i += 1
            print(self.nom, " : je tente ", n, " �cart ", b-a, " � traiter ", self.queue.qsize ())

        # fini
        print(self.nom, " : j'arr�te")
        self.event.set ()
        
# on cr�e des verrous pour attendre la fin de la partie        
e1 = threading.Event ()
e2 = threading.Event ()
e1.clear ()
e2.clear ()

# cr�ation des joueurs
A = Joueur ("A", e1, 10, temps = 0.1)
B = Joueur ("B", e2, 10, temps = 0.3)

# chaque joueur sait qui est l'autre
A.Joueur (B)
B.Joueur (A)

# le jeu commence
A.start ()
B.start ()

# on attend la fin de la partie
e1.wait ()
e2.wait ()