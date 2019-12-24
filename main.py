import sys
from src.solutions.day1 import Day1
from src.solutions.day2 import Day2
from src.solutions.day3 import Day3
from src.solutions.day4 import Day4
from src.solutions.day5 import Day5
from src.solutions.day6 import Day6
from src.solutions.day7 import Day7
from src.solutions.day8 import Day8
from src.solutions.day9 import Day9

if __name__ == '__main__':
    problemNumber = sys.argv[1]
    if (problemNumber == "1-1"):
        print(Day1().part1())
    elif (problemNumber == "1-2"):
        print(Day1().part2())
    elif (problemNumber == "2-1"):
        print(Day2().part1())
    elif (problemNumber == "2-2"):
        print(Day2().part2())
    elif (problemNumber == "3-1"):
        print(Day3().part1())
    elif (problemNumber == "3-2"):
        print(Day3().part2())
    elif (problemNumber == "4-1"):
        print(Day4().part1())
    elif (problemNumber == "4-2"):
        print(Day4().part2())
    elif (problemNumber == "5-1"):
        print(Day5().part1())
    elif (problemNumber == "5-2"):
        print(Day5().part2())
    elif (problemNumber == "6-1"):
        print(Day6().part1())
    elif (problemNumber == "6-2"):
        print(Day6().part2())
    elif (problemNumber == "7-1"):
        print(Day7().part1())
    elif (problemNumber == "7-2"):
        print(Day7().part2())
    elif (problemNumber == "8-1"):
        print(Day8().part1())
    elif (problemNumber == "8-2"):
        print(Day8().part2())
    elif (problemNumber == "9-1"):
        print(Day9().part1())
    elif (problemNumber == "9-2"):
        print(Day9().part2())