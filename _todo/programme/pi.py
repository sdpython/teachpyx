# coding: latin-1
import random
import math

somme = 0
nb    = 1000000
for i in range (0,nb) :
    x = random.random ()  # nombre aléatoire entre [0,1]
    y = random.random ()
    r = math.sqrt (x*x + y*y)  # racine carrée
    if r <= 1 : somme += 1
        
print "estimation ", 4 * float (somme) / nb
print "PI = ", math.pi