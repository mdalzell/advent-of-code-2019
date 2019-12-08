import unittest
from Day1.day1 import calculateFuel, calculateFuelWithAddedMass

class Day1Test(unittest.TestCase):

    def test_calculateFuel_exampleCase1(self):
        self.assertEqual(calculateFuel(12), 2)

    def test_calculateFuel_exampleCase2(self):
        self.assertEqual(calculateFuel(14), 2)

    def test_calculateFuel_exampleCase3(self):
        self.assertEqual(calculateFuel(1969), 654)

    def test_calculateFuel_exampleCase4(self):
        self.assertEqual(calculateFuel(100756), 33583)

    def test_calculateFuelWithAddedMass_exampleCase1(self):
        self.assertEqual(calculateFuelWithAddedMass(12), 2)

    def test_calculateFuelWithAddedMass_exampleCase2(self):
        self.assertEqual(calculateFuelWithAddedMass(1969), 966)

    def test_calculateFuelWithAddedMass_exampleCase3(self):
        self.assertEqual(calculateFuelWithAddedMass(100756), 50346)

if __name__ == '__main__':
    unittest.main()