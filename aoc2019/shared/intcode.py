class IntCode:
    def __init__(self, intList, inputs=None):
        extraMemory = [0] * 100000
        self.__pointer = 0
        self.__inputPointer = 0
        self.__relativeBase = 0
        self.finished = False
        self.inputs = inputs or []
        self.intList = intList + extraMemory
        self.output = []

    def __getMemoryLocation(self, pos, mode):
        arg = self.__pointer + pos
        if mode is 1:
            return arg
        elif mode is 2:
            return self.__relativeBase + self.intList[arg]
        else:
            return self.intList[arg]

    def run(self):
        while not self.finished:
            opcodeString = str(self.intList[self.__pointer])
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
            if opcode == 1:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                param2 = self.intList[self.__getMemoryLocation(2, mode2)]
                self.intList[self.__getMemoryLocation(
                    3, mode3)] = param1 + param2
                step += 4
            elif opcode == 2:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                param2 = self.intList[self.__getMemoryLocation(2, mode2)]
                self.intList[self.__getMemoryLocation(
                    3, mode3)] = param1 * param2
                step += 4
            elif opcode == 3:
                if self.__inputPointer < len(self.inputs):
                    inputVal = self.inputs[self.__inputPointer]
                    self.intList[self.__getMemoryLocation(
                        1, mode1)] = int(inputVal)
                    self.__inputPointer += 1
                    step += 2
                else:
                    return
            elif opcode == 4:
                printVal = self.intList[self.__getMemoryLocation(1, mode1)]
                self.output.append(printVal)
                step += 2
            elif opcode == 5:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                param2 = self.intList[self.__getMemoryLocation(2, mode2)]
                if param1 != 0:
                    self.__pointer = param2
                else:
                    step += 3
            elif opcode == 6:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                param2 = self.intList[self.__getMemoryLocation(2, mode2)]
                if param1 == 0:
                    self.__pointer = param2
                else:
                    step += 3
            elif opcode == 7:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                param2 = self.intList[self.__getMemoryLocation(2, mode2)]
                self.intList[self.__getMemoryLocation(
                    3, mode3)] = 1 if param1 < param2 else 0
                step += 4
            elif opcode == 8:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                param2 = self.intList[self.__getMemoryLocation(2, mode2)]
                self.intList[self.__getMemoryLocation(
                    3, mode3)] = 1 if param1 == param2 else 0
                step += 4
            elif opcode == 9:
                param1 = self.intList[self.__getMemoryLocation(1, mode1)]
                self.__relativeBase += param1
                step += 2
            elif opcode == 99:
                self.finished = True
                return

            self.__pointer += step
