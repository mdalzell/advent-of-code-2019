from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day23 import buildNetwork, findFirstPacketToAddress, findFirstRepeatedNatValue


class Day23(Solution):
    def part1(self):
        network = self.__buildNetwork()
        packet = findFirstPacketToAddress(network, 255)
        return packet.y

    def part2(self):
        network = self.__buildNetwork()
        return findFirstRepeatedNatValue(network)

    def __buildNetwork(self):
        program = getProgramFromFile(self._dirPath + "/../input/day23.txt")
        return buildNetwork(program)
