import unittest
from src.helpers.day3 import calculateMinSignalDelay, calculateManhattanDistance


class Day3Test(unittest.TestCase):

    def test_calculateManhattanDistance_exampleCase1(self):
        self.assertEqual(
            calculateManhattanDistance(
                'R75,D30,R83,U83,L12,D49,R71,U7,L72',
                'U62,R66,U55,R34,D71,R55,D58,R83'),
            159)

    def test_calculateManhattanDistance_exampleCase2(self):
        self.assertEqual(
            calculateManhattanDistance(
                'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'),
            135)

    def test_calculateMinSignalDelay_exampleCase1(self):
        self.assertEqual(
            calculateMinSignalDelay(
                'R75,D30,R83,U83,L12,D49,R71,U7,L72',
                'U62,R66,U55,R34,D71,R55,D58,R83'),
            610)

    def test_calculateMinSignalDelay_exampleCase2(self):
        self.assertEqual(
            calculateMinSignalDelay(
                'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'),
            410)


if __name__ == '__main__':
    unittest.main()
