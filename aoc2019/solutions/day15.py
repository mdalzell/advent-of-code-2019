from aoc2019.helpers.day15 import RepairDroid, calculateMinutesToFullOxygen
from aoc2019.shared.solution import Solution


class Day15(Solution):
    def part1(self):
        program = self.__getProgram()
        droid = RepairDroid(program)
        droid.findOxygenSystem()
        return droid.minStepsToOxygenSystem

    def part2(self):
        program = self.__getProgram()
        droid = RepairDroid(program)
        droid.findOxygenSystem()
        shipMap = droid.visitedPositions
        oxygenSystemLocation = droid.oxygenSystemLocation
        return calculateMinutesToFullOxygen(oxygenSystemLocation, shipMap)

    def __getProgram(self):
        program = []
        with open(self._dirPath + "/../input/day15.txt") as input:
            for line in input:
                program = list(map(int, line.split(',')))
        return program
