import unittest
from contextlib import redirect_stdout
from io import StringIO
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.practice.tsp_kruskal import (
    simulation,
    equation_droite,
    evaluation_droite,
    intersection_segment,
    construit_ville,
    tsp_kruskal_algorithm,
)


class TestTspKruskal(ExtTestCase):
    def test_equation_droite(self):
        res = equation_droite((0.0, 0.0), (1.0, 1.0))
        self.assertEqual(res, (1.0, -1.0, 0.0))
        ev = evaluation_droite(*res, (0.0, 1.0))
        self.assertEqual(ev, -1.0)
        inter = intersection_segment((0.0, 0.0), (1.0, 1.0), (0.0, 1.0), (1.0, 0.0))
        self.assertTrue(inter)
        inter = intersection_segment((0.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.1, 1.1))
        self.assertFalse(inter)

    def test_kruskal(self):
        nb_ville = 700
        x, y = 800, 500
        villes = construit_ville(nb_ville, x, y)
        neurones = tsp_kruskal_algorithm(villes, max_iter=10)
        self.assertEqual(len(villes), len(neurones))

    def test_kruskal_simulation(self):
        st = StringIO()
        with redirect_stdout(st):
            villes, points = simulation(nb=5, verbose=2, max_iter=5000)
        self.assertEqual(len(villes), 5)
        self.assertEqual(len(points), 5)
        text = st.getvalue()
        self.assertIn("[tsp_kruskal_algorithm]", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
