import sys

def calculateMinSignalDelay(wire1, wire2):
    wire1pointsList = convertWireStringToPointSet(wire1)
    wire2pointsList = convertWireStringToPointSet(wire2)
    intersection = findIntersection(wire1pointsList, wire2pointsList)

    minDistance = sys.maxsize
    for point in intersection:
        distance = wire1pointsList.index(point) + wire2pointsList.index(point) + 2
        if distance < minDistance:
            minDistance = distance

    return minDistance

def calculateManhattanDistance(wire1, wire2):
    wire1pointsList = convertWireStringToPointSet(wire1)
    wire2pointsList = convertWireStringToPointSet(wire2)
    intersection = findIntersection(wire1pointsList, wire2pointsList)

    minDistance = sys.maxsize
    for point in intersection:
        distance = abs(point[0]) + abs(point[1])
        if distance < minDistance:
            minDistance = distance

    return minDistance


def convertWireStringToPointSet(wire):
    pointArray = []
    currentCoordinate = (0, 0)
    wireCoordinates = wire.split(',')

    for wireCoordinate in wireCoordinates:
        direction = wireCoordinate[0]
        magnitude = int(wireCoordinate[1:])
        if direction == 'R':
            for x in range(currentCoordinate[0] + 1, currentCoordinate[0] + magnitude + 1):
                currentCoordinate = (x, currentCoordinate[1])
                pointArray.append(currentCoordinate)
        elif direction == 'L':
            for x in range(currentCoordinate[0] - 1, currentCoordinate[0] - magnitude - 1, -1):
                currentCoordinate = (x, currentCoordinate[1])
                pointArray.append(currentCoordinate)
        elif direction == 'U':
            for y in range(currentCoordinate[1] + 1, currentCoordinate[1] + magnitude + 1):
                currentCoordinate = (currentCoordinate[0], y)
                pointArray.append(currentCoordinate)
        elif direction == 'D':
            for y in range(currentCoordinate[1] - 1, currentCoordinate[1] - magnitude - 1, -1):
                currentCoordinate = (currentCoordinate[0], y)
                pointArray.append(currentCoordinate)

    return pointArray

def findIntersection(wire1, wire2):
    wire1points = set(wire1)
    wire2points = set(wire2)
    return wire1points.intersection(wire2points)

if __name__ == '__main__':
    wireStrings = []
    with open("./input.txt") as input:
        for line in input:
            wireStrings.append(line)

    if (len(sys.argv) > 1 and sys.argv[1] == "part2"):
        result = calculateMinSignalDelay(wireStrings[0], wireStrings[1])
        print(result)
    else:
        result = calculateManhattanDistance(wireStrings[0], wireStrings[1])
        print(result)

