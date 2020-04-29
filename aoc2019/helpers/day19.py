from aoc2019.shared.intcode import IntCode

class TractorBeam:
    def __init__(self, program):
        self.__computer = IntCode(program)

    def countBeamAreaInGrid(self, gridSize):
        points = 0

        for x in range(0, gridSize):
            for y in range(0, gridSize):
                if self.__isPointInBeam(x, y):
                    points += 1

        return points

    # Trace the bottom of the line, then check if the upper corner is also in the beam
    def getClosestPointOfShipToEmitter(self, shipSize):
        y = shipSize - 1
        x = 0
        while True:
            if self.__isPointInBeam(x, y):
                if self.__isPointInBeam(x + shipSize - 1, y - shipSize + 1):
                    return [x, y - shipSize + 1]
                else: 
                    y += 1
            else:
                x += 1

    def __isPointInBeam(self, x, y):
        self.__computer.inputs += [x, y]
        self.__computer.run()
        output = self.__computer.output[-1]

        self.__computer.reset()
        return output is 1
