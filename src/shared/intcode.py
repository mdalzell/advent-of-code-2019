def intcode(intList):
    pointer = 0
    while pointer < len(intList) - 1:
        opcodeString = str(intList[pointer])
        opcodeLastIndex = len(opcodeString) - 1
        opcode =  int(opcodeString[-2:]) if len(opcodeString) > 1 else int(opcodeString[opcodeLastIndex])
        mode1 = int(opcodeString[opcodeLastIndex - 2]) if len(opcodeString) > 2 else 0
        mode2 = int(opcodeString[opcodeLastIndex - 3]) if len(opcodeString) > 3 else 0

        if opcode == 1:
            val1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            val2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            intList[intList[pointer + 3]] = val1 + val2
        elif opcode == 2:
            val1 = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            val2 = intList[pointer + 2] if mode2 == 1 else intList[intList[pointer + 2]]
            intList[intList[pointer + 3]] = val1 * val2
        elif opcode == 3:
            inputVal = input("Please input a single digit: ")
            intList[intList[pointer + 1]] = int(inputVal)
        elif opcode == 4:
            printVal = intList[pointer + 1] if mode1 == 1 else intList[intList[pointer + 1]]
            print("Opcode 4: " + str(printVal))
        elif opcode == 99:
            break
        
        step = 4 if opcode == 1 or opcode == 2 else 2
        pointer += step

    return intList