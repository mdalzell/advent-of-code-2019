import unittest
from aoc2019.helpers.day12 import Moon, calculateTotalEnergy, findFirstRepeatedState


class Day12Test(unittest.TestCase):

    __exampleCase1MoonList = [
        Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]

    __exampleCase2MoonList = [
        Moon(-8, -10, 0), Moon(5, 5, 10), Moon(2, -7, 3), Moon(9, -8, -3)]

    def test_MoonGetTotalEnergy_ComputesCorrectValue(self):
        moon = Moon(2, 1, 3, 3, 2, 1)
        totalEnergyForMoon = moon.getTotalEnergy()
        self.assertEqual(totalEnergyForMoon, 36)

    def test_calculateTotalEnergy_exampleCase1(self):
        totalEnergy = calculateTotalEnergy(self.__exampleCase1MoonList, 10)
        self.assertEqual(totalEnergy, 179)

    def test_calculateTotalEnergy_exampleCase2(self):
        totalEnergy = calculateTotalEnergy(self.__exampleCase2MoonList, 100)
        self.assertEqual(totalEnergy, 1940)

    def test_findFirstRepeatedState__exampleCase1(self):
        steps = findFirstRepeatedState(self.__exampleCase1MoonList)
        self.assertEqual(steps, 2772)

    def test_findFirstRepeatedState__exampleCase2(self):
        steps = findFirstRepeatedState(self.__exampleCase2MoonList)
        self.assertEqual(steps, 4686774924)


if __name__ == '__main__':
    unittest.main()
