import unittest
from src.shared.intcode import IntCode

class IntcodeTest(unittest.TestCase):

    def test_intcode_exampleCase1(self):
        intCode = IntCode([1,0,0,0,99])
        intCode.run()
        self.assertEqual(intCode.intList, [2,0,0,0,99])

    def test_intcode_exampleCase2(self):
        intCode = IntCode([2,3,0,3,99])
        intCode.run()
        self.assertEqual(intCode.intList, [2,3,0,6,99])

    def test_intcode_exampleCase3(self):
        intCode = IntCode([2,4,4,5,99,0])
        intCode.run()
        self.assertEqual(intCode.intList, [2,4,4,5,99,9801])

    def test_intcode_exampleCase4(self):
        intCode = IntCode([1,1,1,4,99,5,6,0,99])
        intCode.run()
        self.assertEqual(intCode.intList, [30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
    unittest.main()