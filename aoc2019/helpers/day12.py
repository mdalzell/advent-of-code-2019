def calculateTotalEnergy(moonList, steps):

    for _ in range(steps):
        # Apply gravity
        applyGravityToAllMoons(moonList)

        # Update each moon's position based on velocity
        for moon in moonList:
            moon.updatePosition()

    # Return total energy of the system after designated steps
    return sumTotalEnergyForEachMoon(moonList)


def applyGravityToAllMoons(moonList):
    for i in range(0, len(moonList)):
        # Calculate gravity for every moon after it in the list
        for j in range(i + 1, len(moonList)):
            # Apply to each axis
            for k in range(0, 3):
                applyGravity(moonList[i], moonList[j], k)


def applyGravity(moon1, moon2, axis):
    if moon1.position[axis] > moon2.position[axis]:
        moon1.decrementVelocity(axis)
        moon2.incrementVelocity(axis)
    elif moon1.position[axis] < moon2.position[axis]:
        moon1.incrementVelocity(axis)
        moon2.decrementVelocity(axis)


def sumTotalEnergyForEachMoon(moonList):
    totalEnergySum = 0
    for moon in moonList:
        totalEnergySum += moon.getTotalEnergy()

    return totalEnergySum


class Moon:
    def __init__(self, xPos, yPos, zPos, xVel=0, yVel=0, zVel=0):
        self.position = (xPos, yPos, zPos)
        self.__velocity = (xVel, yVel, zVel)

    def getTotalEnergy(self):
        potentialEnergy = abs(
            self.position[0]) + abs(self.position[1]) + abs(self.position[2])
        kineticEnergy = abs(
            self.__velocity[0]) + abs(self.__velocity[1]) + abs(self.__velocity[2])
        return potentialEnergy * kineticEnergy

    def updatePosition(self):
        self.position = tuple(map(sum, zip(self.position, self.__velocity)))

    def incrementVelocity(self, axis):
        newVelocity = [self.__velocity[0],
                       self.__velocity[1], self.__velocity[2]]
        newVelocity[axis] += 1
        self.__velocity = tuple(newVelocity)

    def decrementVelocity(self, axis):
        newVelocity = [self.__velocity[0],
                       self.__velocity[1], self.__velocity[2]]
        newVelocity[axis] -= 1
        self.__velocity = tuple(newVelocity)
