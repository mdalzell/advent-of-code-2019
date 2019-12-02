import math
import sys

def calculateFuel(x):
    return math.floor(x / 3) - 2

def calculateFuelWithAddedMass(x):
    fuel = calculateFuel(x)
    if (fuel <= 0):
        return 0
    return fuel + calculateFuelWithAddedMass(fuel)

def sumFuelCalculations(includeMass):
    fuelSum = 0
    with open("./input.txt") as input:
        for line in input:
            module = int(line)
            if (includeMass):
                fuelSum += calculateFuelWithAddedMass(module)
            else:
                fuelSum += calculateFuel(module)
    print(fuelSum)

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == "includeMass"):
        sumFuelCalculations(True)
    else:
        sumFuelCalculations(False)