from src.shared.intcode import IntCode


def countPanelsPainted(intList):
    intcode = IntCode(intList)
    currentPosition = (0, 0)
    currentDirection = "U"
    hullMap = {}

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

    return len(hullMap)


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
