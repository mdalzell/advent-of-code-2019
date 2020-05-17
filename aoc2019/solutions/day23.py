from aoc2019.shared.solution import Solution
from aoc2019.shared.intcode import getProgramFromFile
from aoc2019.helpers.day23 import buildNetwork, findFirstPacketToAddress


class Day23(Solution):
    def part1(self):
        program = getProgramFromFile(self._dirPath + "/../input/day23.txt")
        network = buildNetwork(program)
        packet = findFirstPacketToAddress(network, 255)
        return packet.y

    def part2(self):
        pass
