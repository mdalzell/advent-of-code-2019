from aoc2019.helpers.day01 import calculateFuel, calculateFuelWithAddedMass
from aoc2019.shared.solution import Solution


class Day1(Solution):
    def __init__(self):
        Solution.__init__(self)
        self.inputPath = self._dirPath + "/../input/day01.txt"

    def part1(self):
        fuelSum = 0
        with open(self.inputPath) as input:
            for line in input:
                fuelSum += calculateFuel(int(line))
        return fuelSum

    def part2(self):
        fuelSum = 0
        with open(self.inputPath) as input:
            for line in input:
                fuelSum += calculateFuelWithAddedMass(int(line))
        return fuelSum
