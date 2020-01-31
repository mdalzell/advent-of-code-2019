from aoc2019.helpers.day03 import calculateManhattanDistance, calculateMinSignalDelay
from aoc2019.shared.solution import Solution


class Day3(Solution):
    def part1(self):
        wires = self.__getWires()
        return calculateManhattanDistance(wires[0], wires[1])

    def part2(self):
        wires = self.__getWires()
        return calculateMinSignalDelay(wires[0], wires[1])

    def __getWires(self):
        wires = []
        with open(self.dirPath + "/../input/day03.txt") as input:
            for line in input:
                wires.append(line)
        return wires
