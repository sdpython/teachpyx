class Fonction :
    def calcul (self, x) : pass
    def calcul_n_valeur (self, l) :
        res = [ self.calcul (i) for i in l ]
        return res
        
class Carre (Fonction) :
    def calcul (self, x) : return x*x
        
class Cube (Fonction) :
    def calcul (self, x) : return x*x*x

l = [0,1,2,3]
print l   # affiche [0, 1, 2, 3]

l1 = Carre ().calcul_n_valeur (l)  # l1 vaut [0, 1, 4, 9]
l2 = Cube () .calcul_n_valeur (l)  # l2 vaut [0, 1, 8, 27]