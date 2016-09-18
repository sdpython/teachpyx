# coding: latin-1
# la première ligne autorise les accents
class fromage :
    
    def __init__ (self, p,c,o) :
        self.poids = p
        self.couleur = c
        self.odeur = o
        
    def decouper (self,nb) :
        l = []
        for i in range (0,nb) :
            f = fromage (self.poids/nb, \
                            self.couleur, self.odeur)
            l.append (f)
        return l

    def __str__ (self) :
        s = "poids : " + str (self.poids)
        s += " couleur : " + str (self.couleur)
        s += " odeur : " + str (self.odeur)
        return s

    def __add__ (self,f) :
        print "ajout fromage"
        poids = self.poids + f.poids
        couleur = [0,0,0]
        for i in range (0,3) :
            couleur [i] = (self.couleur [i] * self.poids \
                       + f.couleur [i] * f.poids) / poids
        odeur = (self.odeur * self.poids + \
                 f.odeur * f.poids) / poids
        couleur = ( couleur [0], couleur [1], couleur [2])
        return fromage (poids, couleur, odeur)

class gruyere (fromage) :
    def __init__ (self,p) :
        fromage.__init__ (self, p, c = (150,150,0), o = 0.1)

    def __str__ (self) :
        s = fromage.__str__(self)
        s = "gruyère, " + s
        return s

    def __add__ (self,f) :
        print "ajout gruyère"
        if not isinstance (f, gruyere) :
            return fromage.__add__ (self, f)
        else :
            r = gruyere (self.poids + f.poids)
            return r

#--------------------------------------------
fr = fromage (5.0, (255,0,0), 0.5)
fr2 = fromage (10.0, (0,255,0), 1)
fr3 = fr + fr2
print fr
print fr2
print fr3
print "----------------------"
g = gruyere (3.0)
g2 = gruyere (7.0)
g3 = g + g2
print g
print g2
print g3
print "----------------------"
print fr2 + g
