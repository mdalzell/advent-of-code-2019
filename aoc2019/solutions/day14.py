from aoc2019.shared.solution import Solution
from aoc2019.helpers.day14 import calculateOreRequiredForFuel, parseInputToFormulaDictionary


class Day14(Solution):
    def part1(self):
        with open(self._dirPath + "/../input/day14.txt") as part1Input:
            formulaDictionary = parseInputToFormulaDictionary(part1Input)
            return calculateOreRequiredForFuel(formulaDictionary)

    def part2(self):
        pass
