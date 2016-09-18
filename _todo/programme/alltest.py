# coding: latin-1
import unittest
import os

def get_test_file () :
    """retourne la liste de tous les fichiers *.py commençant par test_"""
    li = os.listdir (".")
    li = [ l for l in li if "test_" in l and ".py" in l and \
                            ".pyc" not in l and ".pyd" not in l]
    return li

def import_files (li) :
    """pour un fichier test_*.py, cherche les classes Test...
    et crée une suite de test pour ses méthodes commençant 
    par test..., retourne la suite de test"""
    allsuite = []
    for l in li :
        fi = l.replace (".py", "")
        mo = __import__ (fi)
        cl = dir (mo)
        for c in cl :
            if len (c) < 5 or c [:4] != "Test" : continue
            # classe de test c
            testsuite = unittest.TestSuite ()
            exec compile ("di = dir (mo." + c + ")", "", "exec")
            for d in di :
                if len (d) < 5 or d [:4] != "test" : continue
                # method d.c
                exec compile ("t = mo." + c + "(\"" + d + "\")", "", "exec")
                testsuite.addTest (t)
        allsuite.append ((testsuite, l))

    return allsuite

def main () :
    """crée puis lance les suites de textes définis dans 
    des programmes test_*.py"""
    li      = get_test_file ()
    suite   = import_files (li)
    runner  = unittest.TextTestRunner()
    for s in suite :
        print "running test for ", s [1]
        runner.run (s [0])
    
if __name__ == "__main__" :
    main ()