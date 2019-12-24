from src.days.day6 import calculateNumberOfOrbits, getToSanta
from src.shared.solution import Solution

class Day6(Solution):
    def part1(self):
        orbitMap = self.__getOrbitMap()
        return calculateNumberOfOrbits(orbitMap)
    def part2(self):
        orbitMap = self.__getOrbitMap()
        return getToSanta(orbitMap)
    def __getOrbitMap(self):
        orbitMap = []
        with open(self.dirPath + "/../input/day6.txt") as input:
            for line in input:
                orbitMap.append(line.strip('\n'))
        return orbitMap