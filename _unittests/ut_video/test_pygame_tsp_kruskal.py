import unittest
import os
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.video.tsp_kruskal_pygame import pygame_simulation
from teachpyx.tools.display.video_helper import make_video, get_local_folder


class TestLONGTspKruskal(ExtTestCase):
    def test_image_video_kruskal(self):
        import pygame

        flags = pygame.NOFRAME

        temp = get_local_folder(__file__, "temp_kruskal")
        pygame_simulation(
            pygame=pygame,
            folder=temp,
            nb=200 if __name__ == "__main__" else 20,
            size=(400, 250),
            flags=flags,
            verbose=2,
        )
        files = os.listdir(temp)
        self.assertGreater(len(files), 9)
        png = [
            os.path.join(temp, _) for _ in files if os.path.splitext(_)[-1] == ".png"
        ]
        self.assertGreater(len(png), 0)
        out = os.path.join(temp, "tsp_kruskal.avi")
        v = make_video(png, out, size=(200, 125), format="XVID", fps=20)
        self.assertNotEmpty(v)
        self.assertExists(out)


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
