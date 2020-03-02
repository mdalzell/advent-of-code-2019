from aoc2019.shared.solution import Solution
from aoc2019.helpers.day14 import calculateMaxFuelForOre, calculateOreRequiredForFuel, parseInputToFormulaDictionary


class Day14(Solution):
    def part1(self):
        formulaDictionary = self.__getFormulaDictionary()
        return calculateOreRequiredForFuel(formulaDictionary)

    def part2(self):
        formulaDictionary = self.__getFormulaDictionary()
        return calculateMaxFuelForOre(formulaDictionary)

    def __getFormulaDictionary(self):
        with open(self._dirPath + "/../input/day14.txt") as formulaInput:
            return parseInputToFormulaDictionary(formulaInput)
