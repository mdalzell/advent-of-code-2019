from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day19 import countAffectedPoints, getClosestEmitter


class Day19(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day19.txt")
        return countAffectedPoints(program)

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day19.txt")
        return getClosestEmitter(program)
