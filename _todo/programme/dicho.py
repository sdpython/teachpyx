def recherche_dichotomique (li, c) :
    a,b = 0, len (li)-1
    while a <= b :
        m = (a+b)//2
        if   c == li [m] : return m
        elif c <  li [m] : b = m-1   # partie sup�rieure �limin�e
        else             : a = m+1   # partie inf�rieure �limin�e
    return -1  # �l�ment non trouv�
    
li = range (0,100,2)
print (recherche_dichotomique (li, 48))  # affiche 24
print (recherche_dichotomique (li, 49))  # affiche -1