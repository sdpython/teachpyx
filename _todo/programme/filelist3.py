# coding: latin-1
import os
import re

s = r"D:\Dupre\_data\informatique\support\vba\image/vbatd1_4.png"
print re.compile ("[\\\\/]image[\\\\/].*[.]png").search(s)
print re.compile ("[\\\\/]image[\\\\/].*[.]png").match(s)


def liste_fichier_repertoire (folder) :
    file, rep = [], []
    for r, d, f in os.walk (folder) :
        #for a in d : rep.append (r + "/" + a)
        for a in f : 
            e = r + "/" + a
            if re.compile ("[\\\\/]image[\\\\/].*[.]png$").search(e) :
                file.append (r + "/" + a)
    return file, rep
    
folder = r"D:\Dupre\_data\informatique"
file,fold = liste_fichier_repertoire (folder)

for f in file : print "fichier ", f
for f in fold : print "répertoire ", f