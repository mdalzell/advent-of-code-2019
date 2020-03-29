from enum import Enum
from aoc2019.shared.intcode import IntCode


class ASCII(Enum):
    DOT = 46
    HASHTAG = 35
    NEWLINE = 10


def sumAlignmentParametersOfIntersections(scaffoldingMap):
    intersections = set()
    width = len(scaffoldingMap[0])
    height = len(scaffoldingMap)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (scaffoldingMap[i][j] is "#"
                    and scaffoldingMap[i + 1][j] is "#"
                    and scaffoldingMap[i - 1][j] is "#"
                    and scaffoldingMap[i][j + 1] is "#"
                    and scaffoldingMap[i][j - 1] is "#"):
                intersections.add((j, i))

    alignmentParameterSum = 0
    for intersection in intersections:
        alignmentParameterSum += intersection[0] * intersection[1]

    return alignmentParameterSum


class VacuumRobot:
    def __init__(self, program):
        self.__computer = IntCode(program)
        self.map = self.__buildMap()

    def __buildMap(self):
        scaffoldingMap = [""]
        currentLine = 0
        self.__computer.run()

        for result in self.__computer.output:
            if result is ASCII.DOT.value:
                scaffoldingMap[currentLine] += "."
            elif result is ASCII.HASHTAG.value:
                scaffoldingMap[currentLine] += "#"
            elif result is ASCII.NEWLINE.value:
                scaffoldingMap.append("")
                currentLine += 1

        scaffoldingMap = list(filter(None, scaffoldingMap))

        return scaffoldingMap
