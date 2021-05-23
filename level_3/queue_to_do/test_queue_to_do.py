import unittest

from level_3.queue_to_do import answer


class TestQueueToDo(unittest.TestCase):
    def test(self):
        self.assertEqual(answer(0, 3), 2)
        self.assertEqual(answer(17, 4), 14)
