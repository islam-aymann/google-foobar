import unittest

from level_3.fuel_injection_perfection import solution


class TestTheGrandestStaircaseOfThemAll(unittest.TestCase):
    def test(self):
        self.assertEqual(solution('15'), 5)
        self.assertEqual(solution('4'), 2)
        self.assertEqual(solution('768'), 10)
        self.assertEqual(solution('1235'), 15)
        self.assertEqual(solution('65535'), 17)
        self.assertEqual(solution('947712'), 24)
        self.assertEqual(solution('17542149120'), 42)
        self.assertEqual(solution('15755622182313818849280'), 92)
        a = 124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399
        self.assertEqual(solution(str(a)), 1321)