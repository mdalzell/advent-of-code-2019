import unittest
import re
from aoc2019.helpers.day04 import consecutiveDigitsRegex, exactlyTwoConsecutiveDigitsRegex, hasRegexMatch, validPassword


class Day3Test(unittest.TestCase):

    def test_validPassword_exampleCase1(self):
        self.assertEqual(validPassword(111111, consecutiveDigitsRegex), True)

    def test_validPassword_exampleCase2(self):
        self.assertEqual(validPassword(223450, consecutiveDigitsRegex), False)

    def test_validPassword_exampleCase3(self):
        self.assertEqual(validPassword(123789, consecutiveDigitsRegex), False)

    def test_containsExactlyTwoConsecutiveSameDigits_exampleCase1(self):
        self.assertEqual(
            hasRegexMatch(
                112233,
                exactlyTwoConsecutiveDigitsRegex),
            True)

    def test_containsExactlyTwoConsecutiveSameDigits_exampleCase2(self):
        self.assertEqual(
            hasRegexMatch(
                123444,
                exactlyTwoConsecutiveDigitsRegex),
            False)

    def test_containsExactlyTwoConsecutiveSameDigits_exampleCase3(self):
        self.assertEqual(
            hasRegexMatch(
                111122,
                exactlyTwoConsecutiveDigitsRegex),
            True)


if __name__ == '__main__':
    unittest.main()
