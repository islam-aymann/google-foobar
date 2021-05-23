import unittest

from the_cake_is_not_a_lie import solution


class TheCakeIsNotALie(unittest.TestCase):
    def test(self):
        self.assertEqual(solution('abcabcabcabc'), 4)
        self.assertEqual(solution('abccbaabccba'), 2)
        self.assertEqual(solution('abcabcabcabc'), 4)
        self.assertEqual(solution('abccbaabccba'), 2)

        self.assertEqual(solution('a'), 1)
        self.assertEqual(solution('aa'), 2)
        self.assertEqual(solution('abcabc'), 2)
        self.assertEqual(solution('abcabcabc'), 3)
        self.assertEqual(solution('aaT'), 1)
        self.assertEqual(solution('ababT'), 1)
        self.assertEqual(solution('Tabab'), 1)
