import unittest
from aoc2019.shared.intcode import IntCode


class IntcodeTest(unittest.TestCase):

    def test_intcode_exampleCase1(self):
        intCode = IntCode([1, 0, 0, 0, 99])
        intCode.run()
        self.assertEqual(intCode.intList[0], 2)

    def test_intcode_exampleCase2(self):
        intCode = IntCode([2, 3, 0, 3, 99])
        intCode.run()
        self.assertEqual(intCode.intList[3], 6)

    def test_intcode_exampleCase3(self):
        intCode = IntCode([2, 4, 4, 5, 99, 0])
        intCode.run()
        self.assertEqual(intCode.intList[5], 9801)

    def test_intcode_exampleCase4(self):
        intCode = IntCode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        intCode.run()
        self.assertEqual(intCode.intList[0], 30)

    def test_intcode_day9_exampleCase1(self):
        intList = [109, 1, 204, -1, 1001, 100, 1,
                   100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        intCode = IntCode(intList)
        intCode.run()
        self.assertEqual(intCode.output, intList)

    def test_intcode_day9_exampleCase2(self):
        intCode = IntCode([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
        intCode.run()
        self.assertEqual(len(str(intCode.output[0])), 16)

    def test_intcode_day9_exampleCase3(self):
        intCode = IntCode([104, 1125899906842624, 99])
        intCode.run()
        self.assertEqual(intCode.output, [1125899906842624])


if __name__ == '__main__':
    unittest.main()
