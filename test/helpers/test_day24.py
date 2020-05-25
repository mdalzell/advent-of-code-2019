import unittest
from aoc2019.helpers.day24 import calculateBiodiversityRating, getFirstLayoutToAppearTwice

class Day24Test(unittest.TestCase):

    def test_calculateBiodiversityRating_case1(self):
        layoutString = '...../...../...../#..../.#...'
        rating = calculateBiodiversityRating(layoutString)
        self.assertEqual(rating, 2129920)

    def test_getFirstLayoutToAppearTwice_case1(self):
        layoutString = '....#/#..#./#..##/..#../#....'
        repeatedLayout = getFirstLayoutToAppearTwice(layoutString)
        self.assertEqual(repeatedLayout, '...../...../...../#..../.#...')