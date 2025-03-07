import unittest
import os
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.video.tsp_kohonen_pygame import pygame_simulation
from teachpyx.tools.display.video_helper import make_video, get_local_folder


class TestLONGTspKohonen(ExtTestCase):
    def test_image_video_kohonen(self):
        import pygame

        flags = pygame.NOFRAME

        temp = get_local_folder(__file__, "temp_kohonen")
        pygame_simulation(
            pygame,
            folder=temp,
            nb=200 if __name__ == "__main__" else 20,
            size=(400, 250),
            flags=flags,
        )
        files = os.listdir(temp)
        self.assertGreater(len(files), 9)
        png = [
            os.path.join(temp, _) for _ in files if os.path.splitext(_)[-1] == ".png"
        ]
        self.assertGreater(len(png), 0)
        out = os.path.join(temp, "tsp_kohonen.avi")
        v = make_video(png, out, size=(200, 125), format="XVID", fps=20)
        self.assertNotEmpty(v)
        self.assertExists(out)


if __name__ == "__main__":
    unittest.main()
