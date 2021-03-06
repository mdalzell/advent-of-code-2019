import os
import unittest
from aoc2019.helpers.day14 import calculateMaxFuelForOre, calculateOreRequiredForFuel, Formula, parseInputToFormulaDictionary


class Day14Test(unittest.TestCase):

    def test_parseInputToFormulaDictionary(self):
        with open(os.path.dirname(__file__) + "/../input/day14_1.txt") as input:
            testDictionary = {
                'A': Formula(10, [(10, 'ORE')], 'A'),
                'B': Formula(1, [1, 'ORE'], 'B'),
                'C': Formula(1, [(7, 'A'), (1, 'B')], 'C'),
                'D': Formula(1, [(7, 'A'), (1, 'C')], 'D'),
                'E': Formula(1, [(7, 'A'), (1, 'D')], 'E'),
                'FUEL': Formula(1, [(7, 'A'), (1, 'E')], 'FUEL')
            }
            result = parseInputToFormulaDictionary(input)
            self.assertEqual(result['A'].count, testDictionary['A'].count)

    def test_calculateOreRequiredForFuel_1(self):
        with open(os.path.dirname(__file__) + "/../input/day14_1.txt") as input:
            formulaDictionary = parseInputToFormulaDictionary(input)
            oreCount = calculateOreRequiredForFuel(formulaDictionary)
            self.assertEqual(oreCount, 31)

    def test_calculateOreRequiredForFuel_2(self):
        with open(os.path.dirname(__file__) + "/../input/day14_2.txt") as input:
            formulaDictionary = parseInputToFormulaDictionary(input)
            oreCount = calculateOreRequiredForFuel(formulaDictionary)
            self.assertEqual(oreCount, 13312)

    def test_calculateMaxFuelForOre(self):
        with open(os.path.dirname(__file__) + "/../input/day14_2.txt") as input:
            formulaDictionary = parseInputToFormulaDictionary(input)
            maxFuel = calculateMaxFuelForOre(formulaDictionary)
            self.assertEqual(maxFuel, 82892753)


if __name__ == '__main__':
    unittest.main()
