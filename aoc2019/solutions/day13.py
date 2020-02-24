from aoc2019.shared.solution import Solution
from aoc2019.helpers.day13 import countBlockTiles, getScore


class Day13(Solution):
    def part1(self):
        program = self.__getProgram()
        return countBlockTiles(program)

    def part2(self):
        program = self.__getProgram()
        program[0] = 2
        return getScore(program)

    def __getProgram(self):
        program = []
        with open(self._dirPath + "/../input/day13.txt") as input:
            for line in input:
                program = list(map(int, line.split(',')))
        return program
