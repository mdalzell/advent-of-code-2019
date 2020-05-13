import unittest
from aoc2019.helpers.day22 import shuffleNewDeck

class Day22Test(unittest.TestCase):

    def test_shuffleNewDeck_case1(self):
        instructions = ['deal with increment 7', 'deal into new stack', 'deal into new stack']

        result = shuffleNewDeck(10, instructions)
        self.assertEqual(result, [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])

    def test_shuffleNewDeck_case2(self):
        instructions = ['cut 6', 'deal with increment 7', 'deal into new stack']

        result = shuffleNewDeck(10, instructions)
        self.assertEqual(result, [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])

    def test_shuffleNewDeck_case3(self):
        instructions = ['deal with increment 7', 'deal with increment 9', 'cut -2']

        result = shuffleNewDeck(10, instructions)
        self.assertEqual(result, [6, 3, 0, 7, 4, 1, 8, 5, 2, 9])

    def test_shuffleNewDeck_case4(self):
        instructions = ['deal into new stack', 'cut -2', 'deal with increment 7',
                        'cut 8', 'cut -4', 'deal with increment 7', 'cut 3',
                        'deal with increment 9', 'deal with increment 3', 'cut -1']

        result = shuffleNewDeck(10, instructions)
        self.assertEqual(result, [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])