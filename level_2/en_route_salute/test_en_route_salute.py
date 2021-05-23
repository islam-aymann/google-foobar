import unittest

from level_2.en_route_salute import answer


class TheCakeIsNotALie(unittest.TestCase):
    def test(self):
        self.assertEqual(answer('--->-><-><-->-'), 10)
        self.assertEqual(answer('>----<'), 2)
        self.assertEqual(answer('<<>><'), 4)
