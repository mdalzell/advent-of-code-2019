import unittest
from aoc2019.helpers.day18 import minimumStepsToCollectAllKeys

class Day18Test(unittest.TestCase):

    def test_minimumStepsToCollectAllKeys_case1(self):
        scanMap = ['#########', '#b.A.@.a#', '#########']
        result = minimumStepsToCollectAllKeys(scanMap)
        self.assertEqual(result, 8)

    def test_minimumStepsToCollectAllKeys_case2(self):
        scanMap = [
            '########################',
            '#f.D.E.e.C.b.A.@.a.B.c.#',
            '######################.#',
            '#d.....................#',
            '########################'
        ]

        result = minimumStepsToCollectAllKeys(scanMap)
        self.assertEqual(result, 86)

    def test_minimumStepsToCollectAllKeys_case3(self):
        scanMap = [
            '########################',
            '#...............b.C.D.f#',
            '#.######################',
            '#.....@.a.B.c.d.A.e.F.g#',
            '########################'
        ]

        result = minimumStepsToCollectAllKeys(scanMap)
        self.assertEqual(result, 132)

    '''
    def test_minimumStepsToCollectAllKeys_case4(self):
        scanMap = [
            '#################',
            '#i.G..c...e..H.p#',
            '########.########',
            '#j.A..b...f..D.o#',
            '########@########',
            '#k.E..a...g..B.n#',
            '########.########',
            '#l.F..d...h..C.m#',
            '#################'
        ]

        result = minimumStepsToCollectAllKeys(scanMap)
        self.assertEqual(result, 136)
    '''

if __name__ == '__main__':
    unittest.main()
