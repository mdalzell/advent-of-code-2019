import unittest
from aoc2019.helpers.day20 import getMinimumSteps

class Day18Test(unittest.TestCase):

    _testMap = ['         A           ',
        '         A           ',
        '  #######.#########  ',
        '  #######.........#  ',
        '  #######.#######.#  ',
        '  #######.#######.#  ',
        '  #######.#######.#  ',
        '  #####  B    ###.#  ',
        'BC...##  C    ###.#  ',
        '  ##.##       ###.#  ',
        '  ##...DE  F  ###.#  ',
        '  #####    G  ###.#  ',
        '  #########.#####.#  ',
        'DE..#######...###.#  ',
        '  #.#########.###.#  ',
        'FG..#########.....#  ',
        '  ###########.#####  ',
        '             Z       ',
        '             Z       ']

    _testMap2 = ['                   A               ',
        '                   A               ',
        '  #################.#############  ',
        '  #.#...#...................#.#.#  ',
        '  #.#.#.###.###.###.#########.#.#  ',
        '  #.#.#.......#...#.....#.#.#...#  ',
        '  #.#########.###.#####.#.#.###.#  ',
        '  #.............#.#.....#.......#  ',
        '  ###.###########.###.#####.#.#.#  ',
        '  #.....#        A   C    #.#.#.#  ',
        '  #######        S   P    #####.#  ',
        '  #.#...#                 #......VT',
        '  #.#.#.#                 #.#####  ',
        '  #...#.#               YN....#.#  ',
        '  #.###.#                 #####.#  ',
        'DI....#.#                 #.....#  ',
        '  #####.#                 #.###.#  ',
        'ZZ......#               QG....#..AS',
        '  ###.###                 #######  ',
        'JO..#.#.#                 #.....#  ',
        '  #.#.#.#                 ###.#.#  ',
        '  #...#..DI             BU....#..LF',
        '  #####.#                 #.#####  ',
        'YN......#               VT..#....QG',
        '  #.###.#                 #.###.#  ',
        '  #.#...#                 #.....#  ',
        '  ###.###    J L     J    #.#.###  ',
        '  #.....#    O F     P    #.#...#  ',
        '  #.###.#####.#.#####.#####.###.#  ',
        '  #...#.#.#...#.....#.....#.#...#  ',
        '  #.#####.###.###.#.#.#########.#  ',
        '  #...#.#.....#...#.#.#.#.....#.#  ',
        '  #.###.#####.###.###.#.#.#######  ',
        '  #.#.........#...#.............#  ',
        '  #########.###.###.#############  ',
        '           B   J   C               ',
        '           U   P   P               ']

    _testMap3 = ['             Z L X W       C                 ',
        '             Z P Q B       K                 ',
        '  ###########.#.#.#.#######.###############  ',
        '  #...#.......#.#.......#.#.......#.#.#...#  ',
        '  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  ',
        '  #.#...#.#.#...#.#.#...#...#...#.#.......#  ',
        '  #.###.#######.###.###.#.###.###.#.#######  ',
        '  #...#.......#.#...#...#.............#...#  ',
        '  #.#########.#######.#.#######.#######.###  ',
        '  #...#.#    F       R I       Z    #.#.#.#  ',
        '  #.###.#    D       E C       H    #.#.#.#  ',
        '  #.#...#                           #...#.#  ',
        '  #.###.#                           #.###.#  ',
        '  #.#....OA                       WB..#.#..ZH',
        '  #.###.#                           #.#.#.#  ',
        'CJ......#                           #.....#  ',
        '  #######                           #######  ',
        '  #.#....CK                         #......IC',
        '  #.###.#                           #.###.#  ',
        '  #.....#                           #...#.#  ',
        '  ###.###                           #.#.#.#  ',
        'XF....#.#                         RF..#.#.#  ',
        '  #####.#                           #######  ',
        '  #......CJ                       NM..#...#  ',
        '  ###.#.#                           #.###.#  ',
        'RE....#.#                           #......RF',
        '  ###.###        X   X       L      #.#.#.#  ',
        '  #.....#        F   Q       P      #.#.#.#  ',
        '  ###.###########.###.#######.#########.###  ',
        '  #.....#...#.....#.......#...#.....#.#...#  ',
        '  #####.#.###.#######.#######.###.###.#.#.#  ',
        '  #.......#.......#.#.#.#.#...#...#...#.#.#  ',
        '  #####.###.#####.#.#.#.#.###.###.#.###.###  ',
        '  #.......#.....#.#...#...............#...#  ',
        '  #############.#.#.###.###################  ',
        '               A O F   N                     ',
        '               A A D   M                     ']

    def test_getMinimumSteps_case1(self):
        result = getMinimumSteps(self._testMap)
        self.assertEqual(result, 23)

    def test_getMinimumSteps_case2(self):
        result = getMinimumSteps(self._testMap2)
        self.assertEqual(result, 58)

    def test_getMinimumSteps_case3(self):
        result = getMinimumSteps(self._testMap, True)
        self.assertEqual(result, 26)

    def test_getMinimumSteps_case4(self):
        result = getMinimumSteps(self._testMap3, True)
        self.assertEqual(result, 396)