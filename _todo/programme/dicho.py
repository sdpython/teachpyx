def recherche_dichotomique (li, c) :
    a,b = 0, len (li)-1
    while a <= b :
        m = (a+b)//2
        if   c == li [m] : return m
        elif c <  li [m] : b = m-1   # partie supérieure éliminée
        else             : a = m+1   # partie inférieure éliminée
    return -1  # élément non trouvé
    
li = range (0,100,2)
print (recherche_dichotomique (li, 48))  # affiche 24
print (recherche_dichotomique (li, 49))  # affiche -1