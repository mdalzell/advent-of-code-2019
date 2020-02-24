from aoc2019.helpers.day06 import calculateNumberOfOrbits, getToSanta
from aoc2019.shared.solution import Solution


class Day6(Solution):
    def part1(self):
        orbitMap = self.__getOrbitMap()
        return calculateNumberOfOrbits(orbitMap)

    def part2(self):
        orbitMap = self.__getOrbitMap()
        return getToSanta(orbitMap)

    def __getOrbitMap(self):
        orbitMap = []
        with open(self._dirPath + "/../input/day06.txt") as input:
            for line in input:
                orbitMap.append(line.strip('\n'))
        return orbitMap
