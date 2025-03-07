import unittest
from datetime import datetime
from teachpyx.examples.classiques import (
    commentaire_accentues,
    dix_entiers_carre,
    repetition_a_eviter,
    dictionnaire_modifie_dans_la_boucle,
)
from teachpyx.examples.classiques import str2date


class TestClassiques(unittest.TestCase):
    def test_fonctions(self):
        commentaire_accentues()
        r = dix_entiers_carre()
        self.assertEqual(r, 385)
        r = repetition_a_eviter([4, 5], False)
        self.assertEqual(r, 0.25)
        r2 = repetition_a_eviter([4, 5], True)
        self.assertEqual(r2, 0.25)
        r = dictionnaire_modifie_dans_la_boucle()
        self.assertEqual(r, ([0, 1, 2, 4, 5, 6], {0: 0, 1: 1, 2: 2, 5: 5, 6: 6}))
        r = str2date("11/8/1975")
        self.assertEqual(r, datetime(1975, 8, 11))


if __name__ == "__main__":
    unittest.main()
