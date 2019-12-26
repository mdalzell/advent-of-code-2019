import unittest
from src.helpers.day10 import findBestAsteroid, destroyAsteroids

example1 = [
    ".#..#",
    ".....",
    "#####",
    "....#",
    "...##"
]

example2 = ["......#.#.",
            "#..#.#....",
            "..#######.",
            ".#.#.###..",
            ".#..#.....",
            "..#....#.#",
            "#..#....#.",
            ".##.#..###",
            "##...#..#.",
            ".#....####"]

destroyAsteroidExample = [".#..##.###...#######",
                          "##.############..##.",
                          ".#.######.########.#",
                          ".###.#######.####.#.",
                          "#####.##.#.##.###.##",
                          "..#####..#.#########",
                          "####################",
                          "#.####....###.#.#.##",
                          "##.#################",
                          "#####.##.###..####..",
                          "..######..##.#######",
                          "####.##.####...##..#",
                          ".#####..#.######.###",
                          "##...#.##########...",
                          "#.##########.#######",
                          ".####.#.###.###.#.##",
                          "....##.##.###..#####",
                          ".#.#.###########.###",
                          "#.#.#.#####.####.###",
                          "###.##.####.##.#..##"]


class Day10Test(unittest.TestCase):

    def test_findBestAsteroid_exampleCase1(self):
        point, count = findBestAsteroid(example1)
        self.assertEqual(point, (3, 4))
        self.assertEqual(count, 8)

    def test_findBestAsteroid_exampleCase2(self):
        point, count = findBestAsteroid(example2)
        self.assertEqual(point, (5, 8))
        self.assertEqual(count, 33)

    def test_destroyAsteroids_exampleCase1(self):
        destroyedList = destroyAsteroids((11, 13), destroyAsteroidExample)
        self.assertEqual((8, 2), destroyedList[199])


if __name__ == '__main__':
    unittest.main()
