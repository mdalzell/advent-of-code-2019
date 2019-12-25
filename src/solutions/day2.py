from src.helpers.day2 import findNounAndVerb
from src.shared.intcode import IntCode
from src.shared.solution import Solution

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
        with open(self.dirPath + "/../input/day2.txt") as input:
            return list(map(int, input.readline().split(',')))