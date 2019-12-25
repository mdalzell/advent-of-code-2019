from src.helpers.day3 import calculateManhattanDistance, calculateMinSignalDelay
from src.shared.solution import Solution


class Day3(Solution):
    def part1(self):
        wires = self.__getWires()
        return calculateManhattanDistance(wires[0], wires[1])

    def part2(self):
        wires = self.__getWires()
        return calculateMinSignalDelay(wires[0], wires[1])

    def __getWires(self):
        wires = []
        with open(self.dirPath + "/../input/day3.txt") as input:
            for line in input:
                wires.append(line)
        return wires
