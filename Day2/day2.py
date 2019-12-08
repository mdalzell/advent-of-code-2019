import sys

def intcode(intList, noun, verb):
    index = 0
    intList[1] = noun
    intList[2] = verb
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

def findNounAndVerb(intList, desiredOutput):
    intListCopy = intList.copy()
    for noun in range(0, 99):
        for verb in range(0, 99):
            result = intcode(intListCopy, noun, verb)
            if result[0] == desiredOutput:
                print("Noun: " + str(noun))
                print("Verb: " + str(verb))
                return
            else:
                intListCopy = intList.copy()