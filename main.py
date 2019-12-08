import sys
from Day1.day1 import calculateFuel, calculateFuelWithAddedMass
from Day2.day2 import findNounAndVerb, intcode
from Day3.day3 import calculateManhattanDistance, calculateMinSignalDelay
from Day4.day4 import countValidPasswordsInRange, consecutiveDigitsRegex, exactlyTwoConsecutiveDigitsRegex

def day1(isPart2):
    fuelSum = 0
    with open("./Day1/input.txt") as input:
        for line in input:
            module = int(line)
            if (isPart2):
                fuelSum += calculateFuelWithAddedMass(module)
            else:
                fuelSum += calculateFuel(module)
    print(fuelSum)

def day2(isPart2):
    intList = []
    with open("./Day2/input.txt") as input:
        for line in input:
            intList = list(map(int, line.split(',')))

    if (isPart2):
        findNounAndVerb(intList, 19690720)
    else:
        result = intcode(intList, 12, 2)
        print(result)

def day3(isPart2):
    wireStrings = []
    with open("./Day3/input.txt") as input:
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

if __name__ == '__main__':
    problemNumber = sys.argv[1]
    if (problemNumber == "1-1"):
        day1(False)
    elif (problemNumber == "1-2"):
        day1(True)
    elif (problemNumber == "2-1"):
        day2(False)
    elif (problemNumber == "2-2"):
        day2(True)
    elif (problemNumber == "3-1"):
        day3(False)
    elif (problemNumber == "3-2"):
        day3(True)
    elif (problemNumber == "4-1"):
        day4(False)
    elif (problemNumber == "4-2"):
        day4(True)