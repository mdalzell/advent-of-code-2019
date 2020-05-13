from aoc2019.shared.solution import Solution
from aoc2019.helpers.day22 import shuffleNewDeck

class Day22(Solution):
    def part1(self):
        with open(self._dirPath + "/../input/day22.txt") as instructions:
            instructions = instructions.readlines()
            shuffledDeck = shuffleNewDeck(10007, instructions)
            return shuffledDeck.index(2019)

    def part2(self):
        pass
