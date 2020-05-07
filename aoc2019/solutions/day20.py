from aoc2019.shared.solution import Solution
from aoc2019.helpers.day20 import getMinimumSteps

class Day20(Solution):
    def part1(self):
        with open(self._dirPath + "/../input/day20.txt") as maze:
            return getMinimumSteps(maze.readlines())

    def part2(self):
        pass
