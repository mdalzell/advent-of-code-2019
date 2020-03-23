from aoc2019.shared.solution import Solution
from aoc2019.helpers.day16 import decodeRealSignal, improveSignalQuality


class Day16(Solution):
    def part1(self):
        signal = self.__getSignal()
        return improveSignalQuality(signal, 100, 8)

    def part2(self):
        signal = self.__getSignal() * 10000
        startingPosition = int(signal[:7])
        return decodeRealSignal(signal, 100, 8, startingPosition)

    def __getSignal(self):
        with open(self._dirPath + "/../input/day16.txt") as input:
            return input.readline()
