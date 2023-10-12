import unittest
from contextlib import redirect_stdout
from io import StringIO
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.practice.tsp_kohonen import simulation


class TestTspKohonen(ExtTestCase):
    def test_image_video_kohonen(self):
        st = StringIO()
        with redirect_stdout(st):
            villes, neurones = simulation(nb=5, verbose=1, max_iter=5000)
            self.assertEqual(len(villes), 5)
            self.assertIn(len(neurones), (5, 6))
        text = st.getvalue()
        self.assertIn("[simulation]", text)


if __name__ == "__main__":
    unittest.main()
