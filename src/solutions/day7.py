from src.days.day7 import findMaxSignal
from src.shared.solution import Solution

class Day7(Solution):
    def part1(self):
        intList = self.__getProgram()
        return findMaxSignal(intList, 0, 5)
    def part2(self):
        intList = self.__getProgram()
        return findMaxSignal(intList, 5, 10)
    def __getProgram(self):
        with open(self.dirPath + "/../input/day7.txt") as input:
            return list(map(int, input.readline().split(',')))