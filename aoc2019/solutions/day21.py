from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day21 import SpringBot, testSpringCommands

class Day21(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day21.txt")
        springBot = SpringBot(program)
        springBot.loadSpringScript(testSpringCommands)
        return springBot.run()

    def part2(self):
        pass
