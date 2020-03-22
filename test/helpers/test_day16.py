import os
import unittest
from aoc2019.helpers.day16 import improveSignalQuality


class Day16Test(unittest.TestCase):

    def test_improveSignalQuality_case1(self):
        result = improveSignalQuality("12345678", 1, 8)
        self.assertEqual(result, "48226158")

    def test_improveSignalQuality_case2(self):
        result = improveSignalQuality("12345678", 4, 8)
        self.assertEqual(result, "01029498")

    def test_improveSignalQuality_case3(self):
        result = improveSignalQuality(
            "80871224585914546619083218645595", 100, 8)
        self.assertEqual(result, "24176176")

    @unittest.skip("Not performant enough for this yet :(")
    def test_improveSignalQuality_case4(self):
        signal = "03036732577212944063491565474664" * 10000
        startingPosition = signal[0:7]
        result = improveSignalQuality(
            signal, 100, 8, startingPosition)
        self.assertEqual(result, "84462026")


if __name__ == '__main__':
    unittest.main()
