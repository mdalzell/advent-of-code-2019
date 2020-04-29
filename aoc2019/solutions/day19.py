from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day19 import TractorBeam


class Day19(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day19.txt")
        tractorBeam = TractorBeam(program)
        return tractorBeam.countBeamAreaInGrid(50)

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day19.txt")
        tractorBeam = TractorBeam(program)
        point = tractorBeam.getClosestPointOfShipToEmitter(100)
        return point[0] * 10000 + point[1]
