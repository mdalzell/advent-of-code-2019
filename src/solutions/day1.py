from src.days.day1 import calculateFuel, calculateFuelWithAddedMass
from src.shared.solution import Solution

class Day1(Solution):
    def part1(self):
        fuelSum = 0
        with open(self.dirPath + "/../input/day1.txt") as input:
            for line in input:
                fuelSum += calculateFuel(int(line))
        return fuelSum
    def part2(self):
        fuelSum = 0
        with open(self.dirPath + "/../input/day1.txt") as input:
            for line in input:
                fuelSum += calculateFuelWithAddedMass(int(line))
        return fuelSum
