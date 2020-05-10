from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day21 import SpringBot, part1Commands, part2Commands

class Day21(Solution):
    def part1(self):
        return self.__runSpringScript(part1Commands)

    def part2(self):
        return self.__runSpringScript(part2Commands)

    def __runSpringScript(self, commands):
        program = getProgramFromFile(self._dirPath + "/../input/day21.txt")
        springBot = SpringBot(program)
        springBot.loadSpringScript(commands)
        return springBot.run()
