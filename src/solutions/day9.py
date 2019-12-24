from src.shared.intcode import IntCode
from src.shared.solution import Solution

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
        with open(self.dirPath + "/../input/day9.txt") as input:
            for line in input:
                program = list(map(int, line.split(',')))
        return program