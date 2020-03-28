from aoc2019.shared.intcode import IntCode, getProgramFromFile
from aoc2019.shared.solution import Solution


class Day5(Solution):

    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day05.txt")
        intCode = IntCode(program, [1])
        intCode.run()
        return intCode.output

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day05.txt")
        intCode = IntCode(program, [5])
        intCode.run()
        return intCode.output
