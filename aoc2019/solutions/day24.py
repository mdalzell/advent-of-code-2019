from aoc2019.shared.solution import Solution
from aoc2019.helpers.day24 import getFirstLayoutToAppearTwice, calculateBiodiversityRating, countBugsAfterMinutes

class Day24(Solution):
    def part1(self):
        startingLayout = '#..../#...#/##.##/....#/#.##.'
        repeatedLayout = getFirstLayoutToAppearTwice(startingLayout)
        return calculateBiodiversityRating(repeatedLayout)

    def part2(self):
        startingLayout = '#..../#...#/##?##/....#/#.##.'
        return countBugsAfterMinutes(startingLayout, 200)
