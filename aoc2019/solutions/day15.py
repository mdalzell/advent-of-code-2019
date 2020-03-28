from aoc2019.helpers.day15 import RepairDroid, calculateMinutesToFullOxygen
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.shared.solution import Solution


class Day15(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day15.txt")
        droid = RepairDroid(program)
        droid.findOxygenSystem()
        return droid.minStepsToOxygenSystem

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day15.txt")
        droid = RepairDroid(program)
        droid.findOxygenSystem()
        shipMap = droid.visitedPositions
        oxygenSystemLocation = droid.oxygenSystemLocation
        return calculateMinutesToFullOxygen(oxygenSystemLocation, shipMap)
