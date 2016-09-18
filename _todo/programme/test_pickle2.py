import pickle
import copy

class Test :
    def __init__ (self) :
        self.x = 5
        self.y = 3
        self.calcule_norme ()   # attribut calculé
    def calcule_norme (self) :
        self.n = (self.x ** 2 + self.y ** 2) ** 0.5
    def __getstate__ (self) :
        """conversion de Test en un dictionnaire"""
        d = copy.copy (self.__dict__)
        del d ["n"]  # attribut calculé, on le sauve pas
        return d
    def __setstate__ (self,dic) :
        """conversion d'un dictionnaire dic en Test"""
        self.__dict__.update (dic)
        self.calcule_norme ()  # attribut calculé

t = Test ()

f = open('data.bin', 'wb')  # lecture
pickle.dump (t, f)
f.close()

f = open('data.bin', 'rb')  # écriture
t = pickle.load (f)
f.close()