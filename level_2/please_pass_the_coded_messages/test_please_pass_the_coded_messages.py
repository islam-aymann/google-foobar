import unittest

from level_2.please_pass_the_coded_messages import solution


class TestNumbersStationCodedMessages(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([3, 1, 4, 1]), 4311)
        self.assertEqual(solution([3, 1, 4, 1, 5, 9]), 94311)
