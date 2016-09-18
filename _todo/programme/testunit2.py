# coding: latin-1
import unittest
from testunit1 import *

class TestCase_for_addition (unittest.TestCase):
    
    def test_addition_vide (self) :
        """test_addition_vide : on v�rifie que l'addtion de deux listes retourne une liste vide"""
        assert [] == addition ( [], [] )
        
    def test_addition (self) :
        """test_addition : test de [1,2] + [3,-1] != [4,1]"""
        l1 = [1,2]
        l2 = [3,-1]
        l  = addition (l1, l2)
        assert l [0] == 4 and l [1] == 1
        
    def test_exception (self) :
        """test_exception : on v�rifie que l'addition 
        de deux listes de tailles diff�rentes g�n�re une exception"""
        l1 = [1]
        l2 = [3,-1]
        try :
            l  = addition (l1, l2)  # la fonction doit lancer une exception
            assert False            # si elle ne le fait pas, alors le test a achou�
        except Exception, e :
            # on v�rifie que l'exception g�n�r�e n'est pas due � l'instruction assert False
            assert str (e.__class__ .__name__) != "AssertionError"
            # on v�rifie ici que le message de l'exception est celui attendu
            assert str (e) == "listes de tailles diff�rentes"

if __name__ == "__main__" :
    # on lance les tests
    unittest.main ()                       