# coding: latin-1
import os
import re
import mutagen.mp3
import mutagen.easyid3


def infoMP3 (file, tags) :
    """retourne des informations sur un fichier MP3 sous forme de 
    dictionnaire (durée, titre, artiste, ...)"""
    a = mutagen.mp3.MP3(file)
    b = mutagen.easyid3.EasyID3(file)
    info = { "minutes":a.info.length/60, "nom":file }
    for k in tags :
        try: 
            info[k] = str(b[k][0])
        except ValueError: 
            continue
    return info
    
def all_files (repertoire, tags, ext = re.compile (".mp3$")) :
    """retourne les informations pour chaque fichier d'un répertoire"""
    all = []
    for r, d, f in os.walk (repertoire) :
        for a in f : 
            if not ext.search (a): 
                continue
            t = infoMP3(r + "/" + a, tags)
            if len(t) > 0:
                all.append(t)
    return all
    
def heart_notitle_mots (all, avoid,sep,heart) :
    """retourne trois résultats
    - les chansons dont le titre valide l'expression régulière heart
    - les chansons dont le titre valide l'expression régulière avoid
    - le nombre moyen de mots dans le titre d'une chanson"""
    liheart, notitle  = [], []
    nbmot, nbsong     = 0,0
    for a in all :
        if "title" not in a : 
            notitle.append (a)
            continue
        ti = a ["title"].lower ()
        if avoid.match (ti) : 
            notitle.append (a)
            continue
        if heart.search(ti): 
            liheart.append (a)
        nbsong += 1
        nbmot  += len ([ m for m in sep.split (ti) if len (m) > 0 ])
    nbsong = max(nbsong, 1)
    return liheart, notitle, float (nbmot)/nbsong

tags  = "title album artist genre tracknumber".split ()
all = all_files (r"D:\musique", tags)

avoid = re.compile("^(((audio)?track( )?( - )?[0-9]{1,2})|(piste [0-9]{1,2}))$")
sep   = re.compile("[- ,;!'.?&:]")
heart = re.compile("((heart)(?!((ache)|(land))))")
liheart, notitle, moymot = heart_notitle_mots (all, avoid, sep, heart)

print("nombre de mots moyen par titre ", moymot)
print("somme des durée contenant heart ", sum([s ["minutes"] for s in liheart]))
print("chanson sans titre ", len (notitle))
print("liste des titres ")
for s in liheart: 
    print("   ", s["title"])