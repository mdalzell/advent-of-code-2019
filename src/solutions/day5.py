from src.shared.intcode import IntCode
from src.shared.solution import Solution

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
        with open(self.dirPath + "/../input/day5.txt") as input:
            return list(map(int, input.readline().split(',')))