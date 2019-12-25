import math
import sys


def calculateFuel(x):
    return math.floor(x / 3) - 2


def calculateFuelWithAddedMass(x):
    fuel = calculateFuel(x)
    if (fuel <= 0):
        return 0
    return fuel + calculateFuelWithAddedMass(fuel)
