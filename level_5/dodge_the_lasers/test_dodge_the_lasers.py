import unittest

from level_5.dodge_the_lasers import solution


class TestFreeTheBunnyWorkers(unittest.TestCase):
    def test(self):
        self.assertEqual(solution('77'), '4208')
        self.assertEqual(solution('5'), '19')
