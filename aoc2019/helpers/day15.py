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


class RepairDroid:
    def __init__(self):
        self.minStepsToOxygenSystem = None

    def findOxygenSystem(self, program, totalSteps, dirInput):
        computer = IntCode(program)

        if dirInput is not None:
            computer.inputs.append(dirInput)

        computer.run()

        output = computer.output[0]
        updatedProgram = computer.intList

        print('Total Steps: ' + str(totalSteps) + '; Output: ' +
              str(output) + '; Direction: ' + str(dirInput))

        if output is 0:
            return

        if output is 1:
            self.searchInAllDirections(updatedProgram, totalSteps)
            return

        if output is 2:
            if self.minStepsToOxygenSystem is None or totalSteps < self.minStepsToOxygenSystem:
                self.minStepsToOxygenSystem = totalSteps

            return

    def searchInAllDirections(self, program, totalSteps=0):
        updateStepCount = totalSteps + 1
        self.findOxygenSystem(program, updateStepCount, 1)
        self.findOxygenSystem(program, updateStepCount, 2)
        self.findOxygenSystem(program, updateStepCount, 3)
        self.findOxygenSystem(program, updateStepCount, 4)
