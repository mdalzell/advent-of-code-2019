import unittest
from src.days.day7 import findMaxSignal

testInput1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

testInput2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

testInput3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

class Day7Test(unittest.TestCase):

    def test_findHighestSignal_exampleCase1(self):
        self.assertEqual(findMaxSignal(testInput1), 43210)
    
    def test_findHighestSignal_exampleCase2(self):
        self.assertEqual(findMaxSignal(testInput2), 54321)

    def test_findHighestSignal_exampleCase3(self):
        self.assertEqual(findMaxSignal(testInput3), 65210)

if __name__ == '__main__':
    unittest.main()