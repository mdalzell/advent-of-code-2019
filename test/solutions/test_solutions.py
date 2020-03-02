from unittest import mock, TestCase
from aoc2019.solutions import Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14

day8image = [['1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0'],
             ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0',
                 '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],
             ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1',
                 '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0'],
             ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0',
                 '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0'],
             ['1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0',
                 '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],
             ['1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0']]

day11part2 = ([1, 2, 3, 4, 6, 6, 7, 8, 9, 11, 11, 14, 14, 16, 17, 18, 19, 21, 21, 24, 24, 26, 26, 27, 28, 29, 31, 31, 32, 33, 34, 36, 36, 39, 39, 39, 39, 38, 37, 36, 36, 33, 32, 31, 31, 29, 28, 27, 26, 26, 24, 24, 21, 21, 19, 18, 16, 16, 14, 14, 11, 11, 9, 8, 7, 6, 6, 4, 4, 3, 2, 1, 1, 1, 1, 4, 4, 6, 6, 11, 12, 13, 14, 16, 17, 18, 19, 19, 21, 22, 23, 24, 26, 26, 28, 29, 31, 31, 36, 36, 39, 39],
              [-1, 0, 0, -1, -1, 0, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 0, -1, -2, -3, -2, -2, -3, -2, -2, -2, -2, -3, -2, -3, -3, -3, -2, -3, -2, -2, -3, -3, -3, -3, -2, -3, -2, -2, -3, -2, -3, -3, -3, -2, -3, -2, -3, -3, -2, -3, -4, -5, -5, -4, -5, -4, -4, -5, -5, -4, -4, -5, -5, -4, -5, -4, -5, -5, -4, -5, -4, -4, -5, -4, -5, -5, -4, -4, -5])


def plotMock(x, y):
    pass


class SolutionsTest(TestCase):
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

    @mock.patch("aoc2019.solutions.day11.plot", plotMock)
    def test_day11_part2(self):
        self.assertEqual(Day11().part2(), day11part2)

    def test_day12_part1(self):
        self.assertEqual(Day12().part1(), 5937)

    def test_day12_part2(self):
        self.assertEqual(Day12().part2(), 376203951569712)

    def test_day13_part1(self):
        self.assertEqual(Day13().part1(), 312)

    def test_day13_part2(self):
        self.assertEqual(Day13().part2(), 15909)

    def test_day14_part1(self):
        self.assertEqual(Day14().part1(), 857266)

    def test_day14_part2(self):
        self.assertEqual(Day14().part2(), 2144702)
