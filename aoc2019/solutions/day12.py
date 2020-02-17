from aoc2019.shared.solution import Solution
from aoc2019.helpers.day12 import Moon, calculateTotalEnergy


class Day12(Solution):
    def part1(self):
        moon1 = Moon(-6, -5, -8)
        moon2 = Moon(0, -3, -13)
        moon3 = Moon(-15, 10, -11)
        moon4 = Moon(-3, -8, 3)

        return calculateTotalEnergy([moon1, moon2, moon3, moon4], 1000)

    def part2(self):
        pass
