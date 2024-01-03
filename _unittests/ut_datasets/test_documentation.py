import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.datasets.documentation import list_notebooks_rst_links


class TestDocumentation(ExtTestCase):
    def test_documentation_wines(self):
        links = list_notebooks_rst_links("ml", "wines")
        self.assertNotEmpty(links)
        self.assertIn("<nbl-", links[0])
        self.assertIn("wines", links[0])

    def _test_documentation_movie(self):
        links = list_notebooks_rst_links("ml", "movielens")
        self.assertNotEmpty(links)
        self.assertIn("<nbl-", links[0])
        self.assertIn("movielens", links[0])
        self.assertLesser(len(links), 5)


if __name__ == "__main__":
    unittest.main()
