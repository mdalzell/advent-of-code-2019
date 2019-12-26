import math


def asteroidsperQuadrant(coordinate, asteroids):
    quadrant1 = {}
    quadrant2and3 = {}
    quadrant4 = {}
    for asteroid in asteroids:
        rise = asteroid[1] - coordinate[1]
        run = asteroid[0] - coordinate[0]
        arcTan = math.atan2(run, rise)

        if arcTan <= math.pi / 2 and arcTan >= 0:
            if arcTan in quadrant1:
                quadrant1[arcTan].append(asteroid)
            else:
                quadrant1[arcTan] = [asteroid]
        elif arcTan <= math.pi and arcTan > math.pi / 2:
            if arcTan in quadrant4:
                quadrant4[arcTan].append(asteroid)
            else:
                quadrant4[arcTan] = [asteroid]
        else:
            if arcTan in quadrant2and3:
                quadrant2and3[arcTan].append(asteroid)
            else:
                quadrant2and3[arcTan] = [asteroid]

    return quadrant1, quadrant2and3, quadrant4


def detectAsteroids(coordinate, asteroids):
    arcTans = []
    for asteroid in asteroids:
        if asteroid != coordinate:
            rise = asteroid[1] - coordinate[1]
            run = asteroid[0] - coordinate[0]
            arcTan = math.atan2(run, rise)
            arcTans.append(arcTan)
    return len(set(arcTans))


def findBestAsteroid(asteroidGrid):
    bestCoordinate = (0, 0)
    detectedAsteroids = 0
    asteroidCoordinates = findAllAsteroids(asteroidGrid)
    for asteroidCoordinate in asteroidCoordinates:
        count = detectAsteroids(asteroidCoordinate, asteroidCoordinates)
        if count > detectedAsteroids:
            bestCoordinate = asteroidCoordinate
            detectedAsteroids = count

    return bestCoordinate, detectedAsteroids


def destroyAsteroids(coordinate, asteroidGrid):
    destroyedAsteroids = []
    reassignCoordinate(coordinate, asteroidGrid, 'X')
    allAsteroids = findAllAsteroids(asteroidGrid)

    while len(allAsteroids) > 0:
        sortAsteroids(coordinate, allAsteroids)

        quadrant1, quadrant2and3, quadrant4 = asteroidsperQuadrant(
            coordinate, allAsteroids)

        destroyQuadrant(quadrant4, asteroidGrid, destroyedAsteroids)
        destroyQuadrant(quadrant1, asteroidGrid, destroyedAsteroids)
        destroyQuadrant(quadrant2and3, asteroidGrid, destroyedAsteroids)

        # See if any asteroids remaining
        allAsteroids = findAllAsteroids(asteroidGrid)

    return destroyedAsteroids


def destroyQuadrant(quadrant, asteroidGrid, destroyedAsteroids):
    for angle in sorted(quadrant, reverse=True):
        asteroid = quadrant[angle][0]
        reassignCoordinate(asteroid, asteroidGrid, '.')
        destroyedAsteroids.append(asteroid)


def findAllAsteroids(asteroidGrid):
    asteroidCoordinates = []
    for y in range(0, len(asteroidGrid)):
        for x in range(0, len(asteroidGrid[y])):
            if asteroidGrid[y][x] == "#":
                asteroidCoordinates.append((x, y))
    return asteroidCoordinates


def reassignCoordinate(coordinate, asteroidGrid, character):
    lineList = list(asteroidGrid[coordinate[1]])
    lineList[coordinate[0]] = character
    asteroidGrid[coordinate[1]] = ''.join(lineList)


def sortAsteroids(coordinate, asteroids):
    asteroids.sort(key=lambda x: abs(
        x[0] - coordinate[0]) + abs(x[1] - coordinate[1]))
