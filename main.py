import sys
from src.solutions import day1, day2, day3, day4, day5, day6, day7, day8, day9

if __name__ == '__main__':
    problemNumber = sys.argv[1]
    if (problemNumber == "1-1"):
        day1(False)
    elif (problemNumber == "1-2"):
        day1(True)
    elif (problemNumber == "2-1"):
        day2(False)
    elif (problemNumber == "2-2"):
        day2(True)
    elif (problemNumber == "3-1"):
        day3(False)
    elif (problemNumber == "3-2"):
        day3(True)
    elif (problemNumber == "4-1"):
        day4(False)
    elif (problemNumber == "4-2"):
        day4(True)
    elif (problemNumber == "5-1"):
        day5(False)
    elif (problemNumber == "5-2"):
        day5(True)
    elif (problemNumber == "6-1"):
        day6(False)
    elif (problemNumber == "6-2"):
        day6(True)
    elif (problemNumber == "7-1"):
        day7(False)
    elif (problemNumber == "7-2"):
        day7(True)
    elif (problemNumber == "8-1"):
        day8(False)
    elif (problemNumber == "8-2"):
        day8(True)
    elif (problemNumber == "9-1"):
        day9(False)
    elif (problemNumber == "9-2"):
        day9(True)