import unittest

from level_2.numbers_station_coded_messages import answer


class TestNumbersStationCodedMessages(unittest.TestCase):
    def test(self):
        self.assertEqual(answer([4, 3, 5, 7, 8], 12), [0, 2])
        self.assertEqual(answer([4, 3, 10, 2, 8], 12), [2, 3])
        self.assertEqual(answer([1, 2, 3, 4], 15), [-1, -1])
