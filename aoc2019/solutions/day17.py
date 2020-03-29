from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day17 import VacuumRobot, sumAlignmentParametersOfIntersections


class Day17(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day17.txt")
        bot = VacuumRobot(program)

        return sumAlignmentParametersOfIntersections(bot.map)

    def part2(self):
        pass
