# -*- coding: utf-8 -*-
import pickle
import copy

class Test :
    def __init__ (self) :
        self.chaine = "a"
        self.entier = 5
        self.tuple  = { "h":1, 5:"j" }
        
    def __str__(self):
        return "c='{0}' e={1} t={2}".format(self.chaine, self.entier, self.tuple)

t = Test ()

f = open('data.bin', 'wb')  # lecture
pickle.dump (t, f)
f.close()

f = open('data.bin', 'rb')  # écriture
t = pickle.load (f)
f.close()

print(t)