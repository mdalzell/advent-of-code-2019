from aoc2019.helpers.day02 import findNounAndVerb
from aoc2019.shared.intcode import IntCode
from aoc2019.shared.solution import Solution


class Day2(Solution):
    def part1(self):
        program = self.__getProgram()
        program[1] = 12
        program[2] = 2
        intcode = IntCode(program)
        intcode.run()
        return intcode.intList[0]

    def part2(self):
        program = self.__getProgram()
        (noun, verb) = findNounAndVerb(program, 19690720)
        return 100 * noun + verb

    def __getProgram(self):
        with open(self.dirPath + "/../input/day02.txt") as input:
            return list(map(int, input.readline().split(',')))
