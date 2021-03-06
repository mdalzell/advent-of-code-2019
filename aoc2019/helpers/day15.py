from enum import Enum
from aoc2019.shared.intcode import IntCode


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class MoveResult(Enum):
    WALL = 0
    SUCCESS = 1
    OXYGEN_SYSTEM = 2


def calculateMinutesToFullOxygen(oxygenSystemLocation, shipMap):
    currentMinute = 0
    oxygenLocations = set([oxygenSystemLocation])
    visitedLocations = set()

    while len(oxygenLocations) != len(shipMap):
        currentOxygenLocations = oxygenLocations.copy()
        for location in currentOxygenLocations:
            if location not in visitedLocations:
                northLocation = (location[0], location[1] + 1)
                southLocation = (location[0], location[1] - 1)
                westLocation = (location[0] - 1, location[1])
                eastLocation = (location[0] + 1, location[1])

                newLocations = [northLocation, southLocation,
                                westLocation, eastLocation]

                for newLocation in newLocations:
                    if newLocation in shipMap and newLocation not in oxygenLocations:
                        oxygenLocations.add(newLocation)

                visitedLocations.add(location)

        currentMinute = currentMinute + 1

    return currentMinute


class RepairDroid:
    def __init__(self, program):
        self.minStepsToOxygenSystem = None
        self.oxygenSystemLocation = None
        self.visitedPositions = set()
        self.__computer = IntCode(program)
        self.__currentPosition = (0, 0)
        self.__totalSteps = 0

    def findOxygenSystem(self):
        self.__searchInDirection(Direction.NORTH)
        self.__searchInDirection(Direction.SOUTH)
        self.__searchInDirection(Direction.WEST)
        self.__searchInDirection(Direction.EAST)

    def __getReverseDirection(self, direction):
        if direction is Direction.NORTH:
            return Direction.SOUTH
        elif direction is Direction.SOUTH:
            return Direction.NORTH
        elif direction is Direction.WEST:
            return Direction.EAST
        elif direction is Direction.EAST:
            return Direction.WEST

    def __searchInDirection(self, direction):
        self.__computer.inputs.append(direction.value)
        self.__computer.run()

        output = self.__computer.output[-1]

        if output is MoveResult.WALL.value:
            return

        # Move successful, update position
        self.__updatePosition(direction)

        # If returned to origin, this branch search is done
        if self.__currentPosition is (0, 0):
            return

        # Position has not been visited, increment steps.  If a backtrack, decrement and return
        if self.__currentPosition not in self.visitedPositions:
            self.__totalSteps = self.__totalSteps + 1
            self.visitedPositions.add(self.__currentPosition)
        else:
            self.__totalSteps = self.__totalSteps - 1
            return

        if output is MoveResult.OXYGEN_SYSTEM.value:
            if self.oxygenSystemLocation is None:
                self.oxygenSystemLocation = self.__currentPosition
            if self.minStepsToOxygenSystem is None or self.__totalSteps < self.minStepsToOxygenSystem:
                self.minStepsToOxygenSystem = self.__totalSteps

        # Search in all new directions
        reverseDirection = self.__getReverseDirection(direction)

        for newDirection in Direction:
            if newDirection is not reverseDirection:
                self.__searchInDirection(newDirection)

        # Time to back track
        self.__searchInDirection(reverseDirection)

    def __updatePosition(self, direction):
        if direction is Direction.NORTH:
            self.__currentPosition = (
                self.__currentPosition[0], self.__currentPosition[1] + 1)
        elif direction is Direction.SOUTH:
            self.__currentPosition = (
                self.__currentPosition[0], self.__currentPosition[1] - 1)
        elif direction is Direction.WEST:
            self.__currentPosition = (
                self.__currentPosition[0] - 1, self.__currentPosition[1])
        elif direction is Direction.EAST:
            self.__currentPosition = (
                self.__currentPosition[0] + 1, self.__currentPosition[1])
