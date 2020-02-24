from aoc2019.shared.intcode import IntCode
from aoc2019.shared.solution import Solution


class Day5(Solution):
    def part1(self):
        program = self.__getProgram()
        intCode = IntCode(program, [1])
        intCode.run()
        return intCode.output

    def part2(self):
        program = self.__getProgram()
        intCode = IntCode(program, [5])
        intCode.run()
        return intCode.output

    def __getProgram(self):
        with open(self._dirPath + "/../input/day05.txt") as input:
            return list(map(int, input.readline().split(',')))
