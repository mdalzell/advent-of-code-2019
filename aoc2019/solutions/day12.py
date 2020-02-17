from aoc2019.shared.solution import Solution
from aoc2019.helpers.day12 import Moon, calculateTotalEnergy, findFirstRepeatedState


class Day12(Solution):

    __moonList = [Moon(-6, -5, -8), Moon(0, -3, -13),
                  Moon(-15, 10, -11), Moon(-3, -8, 3)]

    def part1(self):
        return calculateTotalEnergy(self.__moonList, 1000)

    def part2(self):
        return findFirstRepeatedState(self.__moonList)
