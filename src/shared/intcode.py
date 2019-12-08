def intcode(intList):
    index = 0
    while index < len(intList) - 1:
        opcode = intList[index]

        if opcode == 1:
            intList[intList[index + 3]] = intList[intList[index + 1]] + intList[intList[index + 2]]
        
        if opcode == 2:
            intList[intList[index + 3]] = intList[intList[index + 1]] * intList[intList[index + 2]]

        if opcode == 99:
            break
        
        index += 4

    return intList