# coding: latin-1
s       = "case11;case12;case13|case21;case22;case23"
ligne   = s.split ("|")
mat     = [ l.split (";") for l in ligne ]
print mat
ligne   = [ ";".join (l) for l in mat ]
s       = "|".join (ligne)
print s

def fonction (x) : return x*x

li = [ 0, 434, 43, 6436, 5 ]
m  = 0
for i in range (0, len (li)) : 
    if li [m] < li [i] : m = i
print li [m]


k = [ (li [i],i) for i in range (0, len (li)) ]
print k
print max (k)

def recherche (li, c) :
    for i in range (0, len (li)) :
        if li [i] == c : return i
    return -1
print recherche (li, 43)

for i in range (0, len (li)) :
    pos = i
    for j in range (i+1, len (li)) :
        if li [j] < li [pos] : pos = j
    ech      = li [pos] 
    li [pos] = li [i]
    li [i]   = ech
print li

li = ["un", "deux", "un", "trois"]
d  = { }
for l in li :
    if l not in d : d [l] = 1
    else : d [l] += 1
print d   # affiche {'un': 2, 'trois': 1, 'deux': 1}

mat = [ [1,1,1], [2,2,2], [1,1,1]]
d  = { }
for l in mat :
    k = str (l)
    if k not in d : d [k] = 1
    else : d [k] += 1
print d   # affiche {'[1, 1, 1]': 2, '[2, 2, 2]': 1}

li = ["un", "deux", "un", "trois"]
d  = { }
for i in range (0, len (li)) :
    if li [i] not in d : d [li [i]] = [ i ]
    else : d [li [i]].append (i)
print d   # affiche {'un': [0, 2], 'trois': [3], 'deux': [1]}
