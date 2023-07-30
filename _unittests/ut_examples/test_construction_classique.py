"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
from teachpyx.examples.construction_classique import (
    recherche,
    minindex,
    text2mat,
    compte,
    integrale,
    vect2mat,
    mat2vect,
    recherche_dichotomique,
    mat2text,
    triindex,
    construit_matrice_carree,
    somme,
)


class TestConstructionClassique(unittest.TestCase):
    def test_fonction(self):
        self.assertEqual(recherche([2, 3, 45], 3), 1)
        self.assertEqual(recherche([2, 3, 45], 4), -1)
        self.assertEqual(minindex([2, 3, 45, -1, 5]), (-1, 3))
        li = range(0, 100, 2)
        self.assertEqual(recherche_dichotomique(li, 48), 24)
        self.assertEqual(recherche_dichotomique(li, 49), -1)
        s = "case11;case12;case13|case21;case22;case23"
        mat = text2mat(s, "|", ";")
        t = mat2text(mat, "|", ";")
        self.assertEqual(t, s)
        tab = ["zero", "un", "deux"]
        r = triindex(tab)
        self.assertEqual(r, [("deux", 2), ("un", 1), ("zero", 0)])
        li = ["un", "deux", "un", "trois"]
        r = compte(li)
        self.assertEqual(r, {"trois": 1, "deux": 1, "un": 2})
        mat = [[0, 1, 2], [3, 4, 5]]
        r = mat2vect(mat)
        self.assertEqual(r, [0, 1, 2, 3, 4, 5])
        m = vect2mat(r, 3)
        self.assertEqual(m, mat)
        x2 = integrale(lambda x: x, 0, 2, 1000)
        self.assertEqual(x2, 2)

    def test_matrice_carre(self):
        mat = construit_matrice_carree(10)
        self.assertEqual(len(mat), 10)
        self.assertEqual(len(mat[0]), 10)

    def test_somme(self):
        li = [0, 1, 2]
        self.assertEqual(somme(li), 3)


if __name__ == "__main__":
    unittest.main()
