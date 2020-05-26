from unittest import mock, TestCase, skip
import aoc2019.solutions as solutions

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
        self.assertEqual(solutions.Day1().part1(), 3317970)

    def test_day1_part2(self):
        self.assertEqual(solutions.Day1().part2(), 4974073)

    def test_day2_part1(self):
        self.assertEqual(solutions.Day2().part1(), 9581917)

    def test_day2_part2(self):
        self.assertEqual(solutions.Day2().part2(), 2505)

    def test_day3_part1(self):
        self.assertEqual(solutions.Day3().part1(), 1626)

    def test_day3_part2(self):
        self.assertEqual(solutions.Day3().part2(), 27330)

    def test_day4_part1(self):
        self.assertEqual(solutions.Day4().part1(), 1764)

    def test_day4_part2(self):
        self.assertEqual(solutions.Day4().part2(), 1196)

    def test_day5_part1(self):
        self.assertEqual(solutions.Day5().part1(), [0, 0, 0, 0, 0, 0, 0, 0, 0, 16225258])

    def test_day5_part2(self):
        self.assertEqual(solutions.Day5().part2(), [2808771])

    def test_day6_part1(self):
        self.assertEqual(solutions.Day6().part1(), 261306)

    def test_day6_part2(self):
        self.assertEqual(solutions.Day6().part2(), 382)

    def test_day7_part1(self):
        self.assertEqual(solutions.Day7().part1(), 368584)

    def test_day7_part2(self):
        self.assertEqual(solutions.Day7().part2(), 35993240)

    def test_day8_part1(self):
        self.assertEqual(solutions.Day8().part1(), 1792)

    def test_day8_part2(self):
        self.assertEqual(solutions.Day8().part2(), day8image)

    def test_day9_part1(self):
        self.assertEqual(solutions.Day9().part1(), [3454977209])

    def test_day9_part2(self):
        self.assertEqual(solutions.Day9().part2(), [50120])

    def test_day10_part1(self):
        self.assertEqual(solutions.Day10().part1(), ((13, 17), 269))

    def test_day10_part2(self):
        self.assertEqual(solutions.Day10().part2(), 612)

    def test_day11_part1(self):
        self.assertEqual(solutions.Day11().part1(), 1883)

    @mock.patch("aoc2019.solutions.day11.plot", plotMock)
    def test_day11_part2(self):
        x, y = solutions.Day11().part2()
        self.assertEqual(set(x), set(day11part2[0]))
        self.assertEqual(set(y), set(day11part2[1]))

    def test_day12_part1(self):
        self.assertEqual(solutions.Day12().part1(), 5937)

    def test_day12_part2(self):
        self.assertEqual(solutions.Day12().part2(), 376203951569712)

    def test_day13_part1(self):
        self.assertEqual(solutions.Day13().part1(), 312)

    def test_day13_part2(self):
        self.assertEqual(solutions.Day13().part2(), 15909)

    def test_day14_part1(self):
        self.assertEqual(solutions.Day14().part1(), 857266)

    def test_day14_part2(self):
        self.assertEqual(solutions.Day14().part2(), 2144702)

    def test_day15_part1(self):
        self.assertEqual(solutions.Day15().part1(), 224)

    def test_day15_part2(self):
        self.assertEqual(solutions.Day15().part2(), 284)

    def test_day16_part1(self):
        self.assertEqual(solutions.Day16().part1(), "42205986")

    def test_day16_part2(self):
        self.assertEqual(solutions.Day16().part2(), "13270205")

    def test_day17_part1(self):
        self.assertEqual(solutions.Day17().part1(), 11140)

    def test_day17_part2(self):
        self.assertEqual(solutions.Day17().part2(), 1113108)

    @skip("Too slow to test :(")
    def test_day18_part1(self):
        self.assertEqual(solutions.Day18().part1(), 6286)

    @skip("Too slow to test :(")
    def test_day18_part2(self):
        self.assertEqual(solutions.Day18().part2(), 2140)

    def test_day19_part1(self):
        self.assertEqual(solutions.Day19().part1(), 131)

    def test_day19_part2(self):
        self.assertEqual(solutions.Day19().part2(), 15231022)

    def test_day20_part1(self):
        self.assertEqual(solutions.Day20().part1(), 578)

    def test_day20_part2(self):
        self.assertEqual(solutions.Day20().part2(), 6592)

    def test_day21_part1(self):
        self.assertEqual(solutions.Day21().part1(), 19354890)

    def test_day21_part2(self):
        self.assertEqual(solutions.Day21().part2(), 1140664209)

    def test_day22_part1(self):
        self.assertEqual(solutions.Day22().part1(), 6289)

    def test_day22_part2(self):
        self.assertEqual(solutions.Day22().part2(), 58348342289943)

    def test_day23_part1(self):
        self.assertEqual(solutions.Day23().part1(), 18513)

    def test_day23_part2(self):
        self.assertEqual(solutions.Day23().part2(), 13286)

    def test_day24_part1(self):
        self.assertEqual(solutions.Day24().part1(), 7543003)

    def test_day24_part2(self):
        self.assertEqual(solutions.Day24().part2(), 1975)
