import random  # import du module random : simulation du hasard
import math    # import du module math : fonctions mathématiques

def integrale_monte_carlo (a,b,f,n) :
    somme = 0.0
    for i in range (0,n) :
        x = random.random () * (b-a) + a
        y = f(x)
        somme += f(x)
    return somme / n
    
def racine (x) : return math.sqrt (x)
    
print integrale (0,1,racine,100000)