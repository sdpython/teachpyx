# coding: latin-1
import glob
import shutil
def copie_repertoire (rep1, rep2) :
    """copie tous les fichiers d'un r�pertoire rep1 vers un autre rep2"""
    li = glob.glob (rep1 + "/*.*")
    for l in li :
        to = l.replace (rep1, rep2)  # nom du fichier copi� 
                                     # (on remplace rep1 par rep2)
        shutil.copy (l, to)
        
import sys
                      # sys.argv [0] --> nom du programme (ici, synchro.py)
rep1 = sys.argv [1]   # r�cup�ration du premier param�tre
rep2 = sys.argv [2]   # r�cup�ration du second param�tre
copie_repertoire (rep1, rep2)