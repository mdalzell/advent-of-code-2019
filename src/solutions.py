import os
from .days.day1 import calculateFuel, calculateFuelWithAddedMass
from .days.day2 import findNounAndVerb
from .days.day3 import calculateManhattanDistance, calculateMinSignalDelay
from .days.day4 import countValidPasswordsInRange, consecutiveDigitsRegex, exactlyTwoConsecutiveDigitsRegex
from .days.day6 import calculateNumberOfOrbits, getToSanta
from .days.day7 import findMaxSignal
from .shared.intcode import IntCode

dirPath = os.path.dirname(os.path.abspath(__file__))

def day1(isPart2):
    fuelSum = 0
    with open(dirPath + "/input/day1-input.txt") as input:
        for line in input:
            module = int(line)
            if (isPart2):
                fuelSum += calculateFuelWithAddedMass(module)
            else:
                fuelSum += calculateFuel(module)
    print(fuelSum)

def day2(isPart2):
    intList = []
    with open(dirPath + "/input/day2-input.txt") as input:
        for line in input:
            intList = list(map(int, line.split(',')))

    if (isPart2):
        findNounAndVerb(intList, 19690720)
    else:
        intList[1] = 12
        intList[2] = 2
        day2intcode = IntCode(intList)
        day2intcode.run()
        print(day2intcode.intList)

def day3(isPart2):
    wireStrings = []
    with open(dirPath + "/input/day3-input.txt") as input:
        for line in input:
            wireStrings.append(line)

    if (isPart2):
        result = calculateMinSignalDelay(wireStrings[0], wireStrings[1])
        print(result)
    else:
        result = calculateManhattanDistance(wireStrings[0], wireStrings[1])
        print(result)

def day4(isPart2):
    if (isPart2):
        print(countValidPasswordsInRange(152085, 670283, exactlyTwoConsecutiveDigitsRegex))
    else:
        print(countValidPasswordsInRange(152085, 670283, consecutiveDigitsRegex))

def day5(isPart2):
    intList = []
    with open(dirPath + "/input/day5-input.txt") as input:
        for line in input:
            intList = list(map(int, line.split(',')))

    inputList = [5] if isPart2 else [1]
    intCode = IntCode(intList, inputList)
    intCode.run()

    print(intCode.output)

def day6(isPart2):
    orbitMap = []
    with open(dirPath + "/input/day6-input.txt") as input:
        for line in input:
            orbitMap.append(line.strip('\n'))

    if (isPart2):
        print(getToSanta(orbitMap))
    else:
        print(calculateNumberOfOrbits(orbitMap))

def day7():
    intList = []
    with open(dirPath + "/input/day7-input.txt") as input:
        for line in input:
            intList = list(map(int, line.split(',')))

    print(findMaxSignal(intList))
