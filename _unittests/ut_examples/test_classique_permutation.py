"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
import itertools
from teachpyx.examples.construction_classique import enumerate_permutations_recursive, enumerate_permutations


class TestClassiquesPermutation (unittest.TestCase):

    def test_permutation(self):
        self.maxDiff = None
        ens = list(range(5))
        lt = list(tuple(p) for p in enumerate_permutations_recursive(ens))
        self.assertEqual(len(lt), 120)
        res = list(tuple(p) for p in itertools.permutations(ens))
        self.assertEqual(len(res), 120)
        self.assertEqual(set(res), set(lt))
        res = list(tuple(p) for p in enumerate_permutations(ens))
        self.assertEqual(len(res), 120)
        self.assertEqual(set(res), set(lt))

        res = list(tuple(p) for p in enumerate_permutations([1]))
        self.assertEqual(res, [(1,)])


if __name__ == "__main__":
    unittest.main()
