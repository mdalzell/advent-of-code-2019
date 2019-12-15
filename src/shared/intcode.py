def intcode(intList, inputs = []):
    pointer = 0
    currentInput = 0
    outputList = []
    while pointer < len(intList) - 1:
        opcodeString = str(intList[pointer])
        opcodeLastIndex = len(opcodeString) - 1
        opcode =  int(opcodeString[-2:]) if len(opcodeString) > 1 else int(opcodeString[opcodeLastIndex])
        mode1 = int(opcodeString[opcodeLastIndex - 2]) if len(opcodeString) > 2 else 0
        mode2 = int(opcodeString[opcodeLastIndex - 3]) if len(opcodeString) > 3 else 0

        step = 0
        if opcode == 1:
            param1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            param2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            intList[intList[pointer + 3]] = param1 + param2
            step += 4
        elif opcode == 2:
            param1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            param2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            intList[intList[pointer + 3]] = param1 * param2
            step += 4
        elif opcode == 3:
            inputVal = inputs[currentInput] if currentInput < len(inputs) else input("Please input the systemID to TEST: ")
            intList[intList[pointer + 1]] = int(inputVal)
            currentInput += 1
            step += 2
        elif opcode == 4:
            printVal = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            outputList.append(printVal)
            step += 2
        elif opcode == 5:
            param1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            param2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            if param1 != 0: 
                pointer = param2 
            else:
                step += 3
        elif opcode == 6:
            param1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            param2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            if param1 == 0: 
                pointer = param2
            else:
                step += 3
        elif opcode == 7:
            param1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            param2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            intList[intList[pointer + 3]] = 1 if param1 < param2 else 0
            step += 4
        elif opcode == 8:
            param1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            param2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            intList[intList[pointer + 3]] = 1 if param1 == param2 else 0
            step += 4
        elif opcode == 99:
            break
        
        pointer += step

    return outputList if len(outputList) is not 0 else intList