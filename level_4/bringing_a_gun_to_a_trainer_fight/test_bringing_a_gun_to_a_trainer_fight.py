import unittest

from level_4.bringing_a_gun_to_a_trainer_fight import solution


class TestFreeTheBunnyWorkers(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([3, 2], [1, 1], [2, 1], 4), 7)
        self.assertEqual(solution([300, 275], [150, 150], [185, 100], 500), 9)
