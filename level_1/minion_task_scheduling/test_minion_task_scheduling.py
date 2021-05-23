from unittest import TestCase

from level_1.minion_task_scheduling.minion_task_scheduling import answer


class TestMinionTaskScheduling(TestCase):
    def test(self):
        self.assertEqual(answer([1, 2, 3], 0), [])
        self.assertEqual(answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1), [1, 4])
        self.assertEqual(answer([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(answer([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(answer([5, 10, 15, 10, 7], 1), [5, 15, 7])
