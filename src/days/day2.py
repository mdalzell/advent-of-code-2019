import sys
from ..shared.intcode import IntCode

def findNounAndVerb(intList, desiredOutput):
    intListCopy = intList.copy()
    for noun in range(0, 99):
        for verb in range(0, 99):
            intListCopy[1] = noun
            intListCopy[2] = verb

            intCode = IntCode(intListCopy)
            intCode.run()
            result = intCode.intList
            if result[0] == desiredOutput:
                print("Noun: " + str(noun))
                print("Verb: " + str(verb))
                return
            else:
                intListCopy = intList.copy()