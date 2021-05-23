import unittest

from level_3.find_the_access_codes import answer
from level_3.find_the_access_codes import answer2


class TestFindTheAccessCodes(unittest.TestCase):
    def test(self):
        self.assertEqual(answer([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(answer([1, 1, 1]), 1)

        self.assertEqual(answer2([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(answer2([1, 1, 1]), 1)
