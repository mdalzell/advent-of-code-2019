import unittest
from src.helpers.day6 import calculateNumberOfOrbits, getToSanta

testOrbit = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L"]

testOrbit2 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    "K)YOU",
    "I)SAN"]


class Day6Test(unittest.TestCase):

    def test_calculateNumberOfOrbits_exampleCase1(self):
        self.assertEqual(calculateNumberOfOrbits(testOrbit), 42)

    def test_getToSanta_exampleCase1(self):
        self.assertEqual(getToSanta(testOrbit2), 4)


if __name__ == '__main__':
    unittest.main()
