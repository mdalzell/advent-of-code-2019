from enum import Enum
from aoc2019.shared.intcode import IntCode


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

    def buildMap(self):
        scaffoldingMap = [""]
        currentLine = 0
        self.__computer.run()

        for result in self.__computer.output:
            if result is 10:
                scaffoldingMap.append("")
                currentLine += 1
            else:
                scaffoldingMap[currentLine] += chr(result)

        scaffoldingMap = list(filter(None, scaffoldingMap))

        return scaffoldingMap

    def __convertCommandToAscii(self, inputCommand):
        asciiInput = ""
        for character in inputCommand:
            asciiInput += str(ord(character))

        asciiInput += "10"
        return int(asciiInput)

    def __convertCommandsToAscii(self, inputCommands):
        asciiInput = []
        for command in inputCommands:
            for character in command:
                asciiInput.append(ord(character))

            asciiInput.append(10)
        return asciiInput

    def collectDust(self, inputCommands):
        inputCommand = self.__convertCommandsToAscii(inputCommands)
        self.__computer.inputs = inputCommand
        self.__computer.run()

        return self.__computer.output[-1]
