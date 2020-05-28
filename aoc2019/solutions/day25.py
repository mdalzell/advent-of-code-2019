from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day25 import RescueBot

class Day25(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day25.txt")
        droid = RescueBot(program)
        droid.beginSearch()

    def part2(self):
        pass
