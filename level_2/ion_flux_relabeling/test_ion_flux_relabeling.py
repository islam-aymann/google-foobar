import unittest

from level_2.ion_flux_relabeling import solution, solution2


class TestIonFluxRelabeling(unittest.TestCase):
    def test(self):
        self.assertEqual(solution(3, [1, 4, 7]), [3, 6, -1])
        self.assertEqual(solution(5, [19, 14, 28]), [21, 15, 29])
        self.assertEqual(solution(3, [7, 3, 5, 1]), [-1, 7, 6, 3])

        self.assertEqual(solution2(3, [1, 4, 7]), [3, 6, -1])
        self.assertEqual(solution2(5, [19, 14, 28]), [21, 15, 29])
        self.assertEqual(solution2(3, [7, 3, 5, 1]), [-1, 7, 6, 3])
