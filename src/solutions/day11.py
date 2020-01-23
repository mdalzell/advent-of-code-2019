from src.shared.solution import Solution
from src.helpers.day11 import countPanelsPainted


class Day11(Solution):
    def part1(self):
        program = []
        with open(self.dirPath + "/../input/day11.txt") as input:
            for line in input:
                program = list(map(int, line.split(',')))

        return countPanelsPainted(program)

    def part2(self):
        pass
