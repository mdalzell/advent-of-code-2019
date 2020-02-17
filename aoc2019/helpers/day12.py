import copy
import math


def calculateTotalEnergy(moonList, steps):

    for _ in range(steps):
        __updateMoons(moonList)

    # Return total energy of the system after designated steps
    return __sumTotalEnergyForEachMoon(moonList)


# In order for state to completely repeat (including velocity), that means there must be a cycle
def findFirstRepeatedState(moonList):

    # Calculate the number of steps in each axis period
    xPeriodSteps = __findPeriodOfAxis(moonList, 0)
    yPeriodSteps = __findPeriodOfAxis(moonList, 1)
    zPeriodSteps = __findPeriodOfAxis(moonList, 2)

    # The first repeated state is when all the cycles of each axis align
    return __lcm(xPeriodSteps, __lcm(yPeriodSteps, zPeriodSteps))


def __findPeriodOfAxis(moonList, axis):
    periodSteps = 0
    universe = copy.deepcopy(moonList)
    foundPeriod = False
    while not foundPeriod:
        __updateMoons(universe)
        periodSteps += 1
        for i in range(0, len(moonList)):
            if universe[i].position[axis] != moonList[i].position[axis] or universe[i].velocity[axis] != moonList[i].velocity[axis]:
                break
            if (i == (len(moonList) - 1)):
                foundPeriod = True

    return periodSteps


def __applyGravityToAllMoons(moonList):
    for i in range(0, len(moonList)):
        # Calculate gravity for every moon after it in the list
        for j in range(i + 1, len(moonList)):
            # Apply to each axis
            for k in range(0, 3):
                __applyGravity(moonList[i], moonList[j], k)


def __applyGravity(moon1, moon2, axis):
    if moon1.position[axis] > moon2.position[axis]:
        moon1.decrementVelocity(axis)
        moon2.incrementVelocity(axis)
    elif moon1.position[axis] < moon2.position[axis]:
        moon1.incrementVelocity(axis)
        moon2.decrementVelocity(axis)


def __sumTotalEnergyForEachMoon(moonList):
    totalEnergySum = 0
    for moon in moonList:
        totalEnergySum += moon.getTotalEnergy()

    return totalEnergySum


def __updateMoons(moonList):
    # Apply gravity
    __applyGravityToAllMoons(moonList)

    # Update each moon's position based on velocity
    for moon in moonList:
        moon.updatePosition()


# Calculates the least common multiple, lifted from here: https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-least-common-multiple
def __lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


class Moon:
    def __init__(self, xPos, yPos, zPos, xVel=0, yVel=0, zVel=0):
        self.position = (xPos, yPos, zPos)
        self.velocity = (xVel, yVel, zVel)

    def getTotalEnergy(self):
        potentialEnergy = abs(
            self.position[0]) + abs(self.position[1]) + abs(self.position[2])
        kineticEnergy = abs(
            self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])
        return potentialEnergy * kineticEnergy

    def updatePosition(self):
        self.position = tuple(map(sum, zip(self.position, self.velocity)))

    def incrementVelocity(self, axis):
        newVelocity = [self.velocity[0],
                       self.velocity[1], self.velocity[2]]
        newVelocity[axis] += 1
        self.velocity = tuple(newVelocity)

    def decrementVelocity(self, axis):
        newVelocity = [self.velocity[0],
                       self.velocity[1], self.velocity[2]]
        newVelocity[axis] -= 1
        self.velocity = tuple(newVelocity)
