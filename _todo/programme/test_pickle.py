import pickle
import copy

class Test :
    def __init__ (self) :
        self.chaine = "a"
        self.entier = 5
        self.tuple  = { "h":1, 5:"j" }

t = Test ()

f = open('data.bin', 'wb')  # lecture
pickle.dump (t, f)
f.close()

f = open('data.bin', 'rb')  # écriture
t = pickle.load (f)
f.close()