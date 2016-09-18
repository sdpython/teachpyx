class Fonction :
    def calcul (self, x) : pass
class Carre (Fonction) :
    def calcul (self, x) : return x*x
class Cube (Fonction) :
    def calcul (self, x) : return x*x*x
        
def calcul_n_valeur (l,f):
    res = [ f(i) for i in l ]
    return res

l = [0,1,2,3]
l1 = calcul_n_valeur (l, Carre ().calcul) # l1 vaut [0, 1, 4, 9]
l2 = calcul_n_valeur (l, Cube ().calcul)  # l2 vaut [0, 1, 8, 27]