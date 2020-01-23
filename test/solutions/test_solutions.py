import unittest
from src.solutions.day1 import Day1
from src.solutions.day2 import Day2
from src.solutions.day3 import Day3
from src.solutions.day4 import Day4
from src.solutions.day5 import Day5
from src.solutions.day6 import Day6
from src.solutions.day7 import Day7
from src.solutions.day8 import Day8
from src.solutions.day9 import Day9
from src.solutions.day10 import Day10
from src.solutions.day11 import Day11

day8image = [['1',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '1',
              '1',
              '0',
              '1',
              '1',
              '1',
              '1',
              '0',
              '0',
              '1',
              '1',
              '0',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0'],
             ['1',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '1',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0'],
             ['1',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '1',
              '1',
              '1',
              '0',
              '0',
              '1',
              '0',
              '0',
              '0',
              '0',
              '1',
              '1',
              '1',
              '1',
              '0'],
             ['1',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '1',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0'],
             ['1',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0',
              '1',
              '0',
              '0',
              '0',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0'],
             ['1',
              '1',
              '1',
              '1',
              '0',
              '0',
              '1',
              '1',
              '0',
              '0',
              '1',
              '1',
              '1',
              '1',
              '0',
              '0',
              '1',
              '1',
              '0',
              '0',
              '1',
              '0',
              '0',
              '1',
              '0']]


class SolutionsTest(unittest.TestCase):
    def test_day1_part1(self):
        self.assertEqual(Day1().part1(), 3317970)

    def test_day1_part2(self):
        self.assertEqual(Day1().part2(), 4974073)

    def test_day2_part1(self):
        self.assertEqual(Day2().part1(), 9581917)

    def test_day2_part2(self):
        self.assertEqual(Day2().part2(), 2505)

    def test_day3_part1(self):
        self.assertEqual(Day3().part1(), 1626)

    def test_day3_part2(self):
        self.assertEqual(Day3().part2(), 27330)

    def test_day4_part1(self):
        self.assertEqual(Day4().part1(), 1764)

    def test_day4_part2(self):
        self.assertEqual(Day4().part2(), 1196)

    def test_day5_part1(self):
        self.assertEqual(Day5().part1(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 16225258])

    def test_day5_part2(self):
        self.assertEqual(Day5().part2(), [2808771])

    def test_day6_part1(self):
        self.assertEqual(Day6().part1(), 261306)

    def test_day6_part2(self):
        self.assertEqual(Day6().part2(), 382)

    def test_day7_part1(self):
        self.assertEqual(Day7().part1(), 368584)

    def test_day7_part2(self):
        self.assertEqual(Day7().part2(), 35993240)

    def test_day8_part1(self):
        self.assertEqual(Day8().part1(), 1792)

    def test_day8_part2(self):
        self.assertEqual(Day8().part2(), day8image)

    def test_day9_part1(self):
        self.assertEqual(Day9().part1(), [3454977209])

    def test_day9_part2(self):
        self.assertEqual(Day9().part2(), [50120])

    def test_day10_part1(self):
        self.assertEqual(Day10().part1(), ((13, 17), 269))

    def test_day10_part2(self):
        self.assertEqual(Day10().part2(), 612)

    def test_day11_part1(self):
        self.assertEqual(Day11().part1(), 1883)
