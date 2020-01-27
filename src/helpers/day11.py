import matplotlib.pyplot as plot
from src.shared.intcode import IntCode


def paintPanels(intList, initialColor):
    intcode = IntCode(intList)
    currentPosition = (0, 0)
    currentDirection = "U"
    hullMap = {
        (0, 0): initialColor
    }

    while not intcode.finished:
        currentColor = hullMap.get(currentPosition, 0)
        intcode.inputs.append(currentColor)

        intcode.run()

        paintColor = intcode.output[-2]
        turnDirection = intcode.output[-1]

        hullMap[currentPosition] = paintColor
        currentDirection = calculateNewDirection(
            currentDirection, turnDirection)
        currentPosition = calculateNewPosition(
            currentPosition, currentDirection)
    return hullMap


def plotPoints(hullMap):
    x, y = getHullPoints(hullMap)
    plot.plot(x, y, 'ro')
    plot.axis([0, 50, -10, 10])
    plot.show()


def getHullPoints(hullMap):
    x = []
    y = []
    for key in hullMap:
        if hullMap[key] is 1:
            x.append(key[0])
            y.append(key[1])

    return x, y


def calculateNewDirection(currentDirection, turnDirection):
    directionMap = {
        "U": {
            0: "L",
            1: "R"
        },
        "R": {
            0: "U",
            1: "D"
        },
        "D": {
            0: "R",
            1: "L"
        },
        "L": {
            0: "D",
            1: "U"
        }
    }

    return directionMap[currentDirection][turnDirection]


def calculateNewPosition(currentPosition, direction):
    if direction is "U":
        return (currentPosition[0], currentPosition[1] + 1)
    elif direction is "R":
        return (currentPosition[0] + 1, currentPosition[1])
    elif direction is "D":
        return (currentPosition[0], currentPosition[1] - 1)
    else:
        return (currentPosition[0] - 1, currentPosition[1])
