from aoc2019.helpers.day08 import buildImage, combineLayers, getLayerWithFewestOfDigit, getCountOfDigitInLayer
from aoc2019.shared.solution import Solution


class Day8(Solution):
    def part1(self):
        image = self.__getImage()
        layer = getLayerWithFewestOfDigit(image, '0')
        return getCountOfDigitInLayer(
            layer, '1') * getCountOfDigitInLayer(layer, '2')

    def part2(self):
        image = self.__getImage()
        return combineLayers(image, 25, 6)

    def __getImage(self):
        inputList = None
        with open(self.dirPath + "/../input/day08.txt") as input:
            for line in input:
                inputList = line

        return buildImage(inputList, 25, 6)
