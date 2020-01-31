from aoc2019.helpers.day10 import findBestAsteroid, destroyAsteroids
from aoc2019.shared.solution import Solution


class Day10(Solution):
    def part1(self):
        asteroidGrid = self.__getAsteroidGrid()
        return findBestAsteroid(asteroidGrid)

    def part2(self):
        asteroidGrid = self.__getAsteroidGrid()
        destroyedAsteroid = destroyAsteroids((13, 17), asteroidGrid)[199]
        return destroyedAsteroid[0] * 100 + destroyedAsteroid[1]

    def __getAsteroidGrid(self):
        asteroidGrid = []
        with open(self.dirPath + "/../input/day10.txt") as input:
            for line in input:
                asteroidGrid.append(line.strip('\n'))
        return asteroidGrid
