import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.expose.tsp_kohonen import simulation


class TestTspKohonen(ExtTestCase):
    def test_image_video_kohonen(self):
        villes, neurones = simulation(nb=5, verbose=1, max_iter=5000)
        print(villes)
        print(neurones)
        self.assertEqual(len(villes), 5)
        self.assertIn(len(neurones), (5, 6))

        """
        import pygame
        flags = pygame.NOFRAME

        pygame_simulation(pygame, fLOG=fLOG, folder=temp,
                          nb=200 if __name__ == "__main__" else 20,
                          size=(400, 250), flags=flags)
        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "tsp_kohonen.avi")
        v = make_video(png, out, size=(200, 125), format="XVID", fps=20)
        assert v is not None
        """


if __name__ == "__main__":
    unittest.main()
