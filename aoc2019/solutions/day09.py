from aoc2019.shared.intcode import IntCode
from aoc2019.shared.solution import Solution


class Day9(Solution):
    def part1(self):
        program = self.__getProgram()
        intCode = IntCode(program, [1])
        intCode.run()
        return intCode.output

    def part2(self):
        program = self.__getProgram()
        intCode = IntCode(program, [2])
        intCode.run()
        return intCode.output

    def __getProgram(self):
        program = []
        with open(self._dirPath + "/../input/day09.txt") as input:
            for line in input:
                program = list(map(int, line.split(',')))
        return program
