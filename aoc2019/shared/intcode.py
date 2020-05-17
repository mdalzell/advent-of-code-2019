from enum import Enum

class Mode(Enum):
    POSITION = 1
    RELATIVE = 2

class OpCode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_RELATIVE_BASE = 9
    FINISHED = 99

def getProgramFromFile(filePath):
    with open(filePath) as input:
        return list(map(int, input.readline().split(',')))


class IntCode:
    __memoryBuffer = [0] * 100000

    def __init__(self, program=None, inputs=None):
        self.__initialProgram = program
        self.__setInitialValues(inputs)

    def __getMemoryLocation(self, pos, mode):
        arg = self.__pointer + pos
        if mode is Mode.POSITION.value:
            return arg
        elif mode is Mode.RELATIVE.value:
            return self.__relativeBase + self.program[arg]
        else:
            return self.program[arg]

    def clearOutput(self):
        self.output = []

    def run(self):
        while not self.finished:
            opcodeString = str(self.program[self.__pointer])
            opcodeLastIndex = len(opcodeString) - 1
            opcode = int(
                opcodeString[-2:]) if len(opcodeString) > 1 else int(opcodeString[opcodeLastIndex])
            mode1 = int(opcodeString[opcodeLastIndex - 2]
                        ) if len(opcodeString) > 2 else 0
            mode2 = int(opcodeString[opcodeLastIndex - 3]
                        ) if len(opcodeString) > 3 else 0
            mode3 = int(opcodeString[opcodeLastIndex - 4]
                        ) if len(opcodeString) > 4 else 0

            step = 0
            if opcode == OpCode.ADD.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                param2 = self.program[self.__getMemoryLocation(2, mode2)]
                self.program[self.__getMemoryLocation(
                    3, mode3)] = param1 + param2
                step += 4
            elif opcode == OpCode.MULTIPLY.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                param2 = self.program[self.__getMemoryLocation(2, mode2)]
                self.program[self.__getMemoryLocation(
                    3, mode3)] = param1 * param2
                step += 4
            elif opcode == OpCode.INPUT.value:
                if self.__inputPointer < len(self.inputs):
                    inputVal = self.inputs[self.__inputPointer]
                    self.program[self.__getMemoryLocation(
                        1, mode1)] = int(inputVal)
                    self.__inputPointer += 1
                    step += 2
                else:
                    return
            elif opcode == OpCode.OUTPUT.value:
                printVal = self.program[self.__getMemoryLocation(1, mode1)]
                self.output.append(printVal)
                step += 2
            elif opcode == OpCode.JUMP_IF_TRUE.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                param2 = self.program[self.__getMemoryLocation(2, mode2)]
                if param1 != 0:
                    self.__pointer = param2
                else:
                    step += 3
            elif opcode == OpCode.JUMP_IF_FALSE.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                param2 = self.program[self.__getMemoryLocation(2, mode2)]
                if param1 == 0:
                    self.__pointer = param2
                else:
                    step += 3
            elif opcode == OpCode.LESS_THAN.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                param2 = self.program[self.__getMemoryLocation(2, mode2)]
                self.program[self.__getMemoryLocation(
                    3, mode3)] = 1 if param1 < param2 else 0
                step += 4
            elif opcode == OpCode.EQUALS.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                param2 = self.program[self.__getMemoryLocation(2, mode2)]
                self.program[self.__getMemoryLocation(
                    3, mode3)] = 1 if param1 == param2 else 0
                step += 4
            elif opcode == OpCode.ADJUST_RELATIVE_BASE.value:
                param1 = self.program[self.__getMemoryLocation(1, mode1)]
                self.__relativeBase += param1
                step += 2
            elif opcode == OpCode.FINISHED.value:
                self.finished = True
                return

            self.__pointer += step

    def reset(self, inputs = None):
        self.__setInitialValues(inputs)
        
    def __setInitialValues(self, inputs):
        self.__pointer = 0
        self.__inputPointer = 0
        self.__relativeBase = 0
        self.finished = False
        self.inputs = inputs or []
        self.output = []
        self.program = self.__initialProgram + self.__memoryBuffer
