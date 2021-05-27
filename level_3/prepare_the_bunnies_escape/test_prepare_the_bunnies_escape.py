import unittest

from level_3.prepare_the_bunnies_escape import solution


class TestQueueToDo(unittest.TestCase):
    def test(self):
        self.assertEqual(
            solution(
                [
                    [0, 1, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 0, 0],
                    [1, 1, 1, 0]
                ]
            ),
            7
        )
        self.assertEqual(
            solution(
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]
                ]
            ),
            11
        )
