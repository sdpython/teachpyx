# coding: latin-1
import os

def liste_fichier_repertoire (folder) :
    file, rep = [], []
    for r, d, f in os.walk (folder) :
        for a in d : rep.append (r + "/" + a)
        for a in f : file.append (r + "/" + a)
    return file, rep
    
folder = r"D:\Dupre\_data\informatique"
file,fold = liste_fichier_repertoire (folder)

for f in file : print "fichier ", f
for f in fold : print "répertoire ", f