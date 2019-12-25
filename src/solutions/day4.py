from src.helpers.day4 import countValidPasswordsInRange, consecutiveDigitsRegex, exactlyTwoConsecutiveDigitsRegex
from src.shared.solution import Solution


class Day4(Solution):
    def part1(self):
        return countValidPasswordsInRange(
            152085, 670283, consecutiveDigitsRegex)

    def part2(self):
        return countValidPasswordsInRange(
            152085, 670283, exactlyTwoConsecutiveDigitsRegex)
