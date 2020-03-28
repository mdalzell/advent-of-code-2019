from aoc2019.helpers.day02 import findNounAndVerb
from aoc2019.shared.intcode import IntCode, getProgramFromFile
from aoc2019.shared.solution import Solution


class Day2(Solution):

    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day02.txt")
        program[1] = 12
        program[2] = 2
        intcode = IntCode(program)
        intcode.run()
        return intcode.program[0]

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day02.txt")
        (noun, verb) = findNounAndVerb(program, 19690720)
        return 100 * noun + verb
