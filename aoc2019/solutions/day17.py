from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day17 import VacuumRobot, sumAlignmentParametersOfIntersections


class Day17(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day17.txt")
        bot = VacuumRobot(program)
        scaffoldingMap = bot.buildMap()

        return sumAlignmentParametersOfIntersections(scaffoldingMap)

    def part2(self):
        program = getProgramFromFile(self._dirPath + "/../input/day17.txt")
        program[0] = 2
        bot = VacuumRobot(program)

        # Worked out the correct path for VacuumBot by hand...it was probably faster in the long run
        inputCommands = ["A,A,B,B,C,B,C,B,C,A",
                         "L,10,L,10,R,6",
                         "R,12,L,12,L,12",
                         "L,6,L,10,R,12,R,12",
                         "n"]

        return bot.collectDust(inputCommands)
