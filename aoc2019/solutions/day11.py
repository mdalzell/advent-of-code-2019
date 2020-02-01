from aoc2019.shared import Solution, plot
from aoc2019.helpers.day11 import paintPanels, getHullPoints


class Day11(Solution):
    def part1(self):
        program = self.__getProgram()
        return len(paintPanels(program, 0))

    def part2(self):
        program = self.__getProgram()
        hullMap = paintPanels(program, 1)
        x, y = getHullPoints(hullMap)
        plot(x, y)
        return x, y

    def __getProgram(self):
        program = []
        with open(self.dirPath + "/../input/day11.txt") as input:
            for line in input:
                program = list(map(int, line.split(',')))

        return program
