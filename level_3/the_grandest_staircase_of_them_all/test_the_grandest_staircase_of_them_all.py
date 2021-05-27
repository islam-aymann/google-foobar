import unittest

from level_3.the_grandest_staircase_of_them_all import solution


class TestTheGrandestStaircaseOfThemAll(unittest.TestCase):
    def test(self):
        self.assertEqual(solution(3), 1)
        self.assertEqual(solution(4), 1)
        self.assertEqual(solution(5), 2)
        self.assertEqual(solution(200), 487067745)
