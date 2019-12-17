class IntCode:
    def __init__(self, intList, inputs = []):
        self.__pointer = 0
        self.__inputPointer = 0
        self.finished = False
        self.inputs = inputs
        self.intList = intList
        self.output = []
    
    def run(self):
        while not self.finished:
            opcodeString = str(self.intList[self.__pointer])
            opcodeLastIndex = len(opcodeString) - 1
            opcode =  int(opcodeString[-2:]) if len(opcodeString) > 1 else int(opcodeString[opcodeLastIndex])
            mode1 = int(opcodeString[opcodeLastIndex - 2]) if len(opcodeString) > 2 else 0
            mode2 = int(opcodeString[opcodeLastIndex - 3]) if len(opcodeString) > 3 else 0

            step = 0
            if opcode == 1:
                param1 = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                param2 = self.intList[self.__pointer + 2] if mode2 == 1 else self.intList[self.intList[self.__pointer + 2]]
                self.intList[self.intList[self.__pointer + 3]] = param1 + param2
                step += 4
            elif opcode == 2:
                param1 = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                param2 = self.intList[self.__pointer + 2] if mode2 == 1 else self.intList[self.intList[self.__pointer + 2]]
                self.intList[self.intList[self.__pointer + 3]] = param1 * param2
                step += 4
            elif opcode == 3:
                if self.__inputPointer < len(self.inputs):
                    inputVal = self.inputs[self.__inputPointer] 
                    self.intList[self.intList[self.__pointer + 1]] = int(inputVal)
                    self.__inputPointer += 1
                    step += 2
                else:
                    return
            elif opcode == 4:
                printVal = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                self.output.append(printVal)
                step += 2
            elif opcode == 5:
                param1 = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                param2 = self.intList[self.__pointer + 2] if mode2 == 1 else self.intList[self.intList[self.__pointer + 2]]
                if param1 != 0: 
                    self.__pointer = param2 
                else:
                    step += 3
            elif opcode == 6:
                param1 = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                param2 = self.intList[self.__pointer + 2] if mode2 == 1 else self.intList[self.intList[self.__pointer + 2]]
                if param1 == 0: 
                    self.__pointer = param2
                else:
                    step += 3
            elif opcode == 7:
                param1 = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                param2 = self.intList[self.__pointer + 2] if mode2 == 1 else self.intList[self.intList[self.__pointer + 2]]
                self.intList[self.intList[self.__pointer + 3]] = 1 if param1 < param2 else 0
                step += 4
            elif opcode == 8:
                param1 = self.intList[self.__pointer + 1] if mode1 == 1 else self.intList[self.intList[self.__pointer + 1]]
                param2 = self.intList[self.__pointer + 2] if mode2 == 1 else self.intList[self.intList[self.__pointer + 2]]
                self.intList[self.intList[self.__pointer + 3]] = 1 if param1 == param2 else 0
                step += 4
            elif opcode == 99:
                return
            
            self.__pointer += step
