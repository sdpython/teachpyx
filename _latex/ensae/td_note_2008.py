# coding: utf-8
# la premi�re ligne autorise les accents dans un programme Python
# la langue anglaise est la langue de l'informatique,
# les mots-cl�s de tous les langages
# sont �crits dans cette langue.

####################################
# exercice 1
####################################
#


# question 1
def lit_fichier(file):
    with open(file, "r") as f:
        li = f.readlines()  # d�coupage sous forme de lignes
    res = []
    for i in li:
        s = i.replace("\n", "")
        s = s.split(" ")  # le s�parateur des colonnes est l'espace
        res.append(s)
    return res


mat = lit_fichier("logpdf.txt")
for m in mat[0:5]:  # on affiche les 5 premi�res lignes
    print(m)  # parce que sinon, c'est trop long

# question 2


def compte_date(mat):
    d = {}
    for m in mat:
        date = m[1]  # cl�
        if date in d:
            d[date] += 1
        else:
            d[date] = 1
    return d


dico_date = compte_date(mat)
print(dico_date)

# remarque g�n�rale : si le fichier logpdf.txt contient des lignes
# vides � la fin, il se produira une erreur � la ligne 34 (date = m [1])
# car la matrice mat contiendra des lignes avec une seule colonne et non quatre.
# Il suffit soit de supprimer les lignes vides du fichier logpdf.txt
# soit de ne pas les prendre en compte lors de la lecture de ce fichier.

# question 3
# La m�thode sort trie la liste mais comment ?
# Il est facile de trier une liste de nombres mais une liste de couples de
# nombres ? L'exemple montre que la liste est tri�e selon le premier �l�ment de
# chaque couple. Pour les cas o� deux couples ont un premier �l�ment en commun,
# les �l�ments semblent tri�s selon le second �l�ment. L'exemple suivant le monte :

li = [
    (1, "un"),
    (
        3,
        "deux",
    ),
    (2, "deux"),
    (1, "hun"),
    (1, "un"),
    (-1, "moinsun"),
]
li.sort(reverse=True)
print(li)  # affiche [(3, 'deux'), (2, 'deux'), (1, 'un'),
#          (1, 'un'),   (1, 'hun'), (-1, 'moinsun')]

# question 4


def dix_meilleures(dico):
    # dans cette fonction on cr�e une liste de couples (valeur,cl�) ou
    # la cl� repr�sente une date et valeur le nombre de t�l�chargement
    # pour cette date
    li = []
    for d in dico:
        cle = d
        valeur = dico[cle]
        li.append((valeur, cle))
    li.sort(reverse=True)
    return li[0:10]


dix = dix_meilleures(dico_date)
print(dix)  # la premi�re date est (283, '26/Sep/2007')

# les quatre premi�res dates correspondent aux quatre premiers TD en 2007 � l'ENSAE

# question 5
# la date est en colonne 1, le document en colonne 3
# on fait un copier-coller de la fonction compte_date en changeant un param�tre


def compte_document(mat):
    d = {}
    for m in mat:
        doc = m[3]  # cl�, 3 au lieu de 1 � la question 2
        if doc in d:
            d[doc] += 1
        else:
            d[doc] = 1
    return d


dix = dix_meilleures(compte_document(mat))
print(dix)  # le premier document est
# (323, '/mywiki/Enseignements?.....target=python_cours.pdf'),

# question 6


def heure(s):
    hs = s[0:2]  # on extrait la partie correspondant � l'heure
    return int(hs)  # on retourne la conversion sous forme d'entiers


# question 7
# on recommence avec un copier-coller


def compte_heure(mat):
    d = {}
    for m in mat:
        h = m[2]  # cl�, 2 au lieu de 1 � la question 2
        cle = heure(h)
        if cle in d:
            d[cle] += 1
        else:
            d[cle] = 1
    return d


h = compte_heure(mat)
dix = dix_meilleures(h)
# la premi�re heure est  (432, 17), ce qui correspond � l'heure des TD
print(dix)

for i in h:
    print(i, "h  ", h[i])

# Il y a beaucoup plus de t�l�chargement entre 20h et 2h du matin
# que le matin avant 10h.
# Le site est plut�t consult� le soir.
# La conclusion ne serait pas aussi �vidente avec un site consult� par des gens
# du monde entier puisque 6h du matin est une heure de l'apr�s midi au Japon.
# Il faudrait croiser l'heure avec la position g�ographique de la personne
# qui consulte le site.
