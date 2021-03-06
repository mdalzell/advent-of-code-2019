from aoc2019.shared.solution import Solution
from aoc2019.helpers.day18 import minimumStepsToCollectAllKeys, correctMapData

class Day18(Solution):
    def part1(self):
        with open(self._dirPath + "/../input/day18.txt") as scanMap:
            return minimumStepsToCollectAllKeys(scanMap.readlines())

    def part2(self):
         with open(self._dirPath + "/../input/day18.txt") as scanMap:
            correctedMap = correctMapData(scanMap.readlines())
            return minimumStepsToCollectAllKeys(correctedMap)
