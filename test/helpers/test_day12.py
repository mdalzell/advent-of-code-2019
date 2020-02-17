import unittest
from aoc2019.helpers.day12 import Moon, calculateTotalEnergy


class Day12Test(unittest.TestCase):

    def test_MoonGetTotalEnergy_ComputesCorrectValue(self):
        moon = Moon(2, 1, 3, 3, 2, 1)
        totalEnergyForMoon = moon.getTotalEnergy()
        self.assertEqual(totalEnergyForMoon, 36)

    def test_calculateTotalEnergy_exampleCase1(self):
        moon1 = Moon(-1, 0, 2)
        moon2 = Moon(2, -10, -7)
        moon3 = Moon(4, -8, 8)
        moon4 = Moon(3, 5, -1)

        totalEnergy = calculateTotalEnergy([moon1, moon2, moon3, moon4], 10)
        self.assertEqual(totalEnergy, 179)

    def test_calculateTotalEnergy_exampleCase2(self):
        moon1 = Moon(-8, -10, 0)
        moon2 = Moon(5, 5, 10)
        moon3 = Moon(2, -7, 3)
        moon4 = Moon(9, -8, -3)

        totalEnergy = calculateTotalEnergy([moon1, moon2, moon3, moon4], 100)
        self.assertEqual(totalEnergy, 1940)


if __name__ == '__main__':
    unittest.main()
