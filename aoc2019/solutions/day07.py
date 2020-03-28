from aoc2019.helpers.day07 import findMaxSignal
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.shared.solution import Solution


class Day7(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day07.txt")
        return findMaxSignal(program, 0, 5)

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day07.txt")
        return findMaxSignal(program, 5, 10)
