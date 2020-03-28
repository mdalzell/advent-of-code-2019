from aoc2019.shared import Solution, plot
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day11 import paintPanels, getHullPoints


class Day11(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day11.txt")
        return len(paintPanels(program, 0))

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day11.txt")
        hullMap = paintPanels(program, 1)
        x, y = getHullPoints(hullMap)
        plot(x, y)
        return x, y
