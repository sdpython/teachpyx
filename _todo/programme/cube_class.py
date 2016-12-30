class Fonction :
    def calcul(self, x):
        pass
    def calcul_n_valeur(self, l) :
        res = [ self.calcul(i) for i in l ]
        return res
        
class Carre (Fonction) :
    def calcul(self, x):
        return x*x
        
class Cube (Fonction) :
    def calcul(self, x):
        return x*x*x

li = [0,1,2,3]
print(li)   # affiche [0, 1, 2, 3]

l1 = Carre().calcul_n_valeur(li)  # l1 vaut [0, 1, 4, 9]
l2 = Cube().calcul_n_valeur(li)   # l2 vaut [0, 1, 8, 27]
print(l1)
print(l2)
