from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day13 import countBlockTiles, getScore


class Day13(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day13.txt")
        return countBlockTiles(program)

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day13.txt")
        program[0] = 2
        return getScore(program)
