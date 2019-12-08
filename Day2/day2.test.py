import unittest
from day2 import intcode 

class Day2Test(unittest.TestCase):

    def test_intcode_exampleCase1(self):
        self.assertEqual(intcode([1,0,0,0,99], 0, 0), [2,0,0,0,99])

    def test_intcode_exampleCase2(self):
        self.assertEqual(intcode([2,3,0,3,99], 3, 0), [2,3,0,6,99])

    def test_intcode_exampleCase3(self):
        self.assertEqual(intcode([2,4,4,5,99,0], 4, 4), [2,4,4,5,99,9801])

    def test_intcode_exampleCase4(self):
        self.assertEqual(intcode([1,1,1,4,99,5,6,0,99], 1, 1), [30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
    unittest.main()