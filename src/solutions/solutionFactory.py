from src.solutions.day1 import Day1
from src.solutions.day2 import Day2
from src.solutions.day3 import Day3
from src.solutions.day4 import Day4
from src.solutions.day5 import Day5
from src.solutions.day6 import Day6
from src.solutions.day7 import Day7
from src.solutions.day8 import Day8
from src.solutions.day9 import Day9
from src.solutions.day10 import Day10
from src.solutions.day11 import Day11
from src.solutions.day12 import Day12
from src.solutions.day13 import Day13
from src.solutions.day14 import Day14
from src.solutions.day15 import Day15
from src.solutions.day16 import Day16
from src.solutions.day17 import Day17
from src.solutions.day18 import Day18
from src.solutions.day19 import Day19
from src.solutions.day20 import Day20
from src.solutions.day21 import Day21
from src.solutions.day22 import Day22
from src.solutions.day23 import Day23
from src.solutions.day24 import Day24
from src.solutions.day25 import Day25


class SolutionFactory:
    def __init__(self):
        self.__solutionMap = {
            "1": Day1,
            "2": Day2,
            "3": Day3,
            "4": Day4,
            "5": Day5,
            "6": Day6,
            "7": Day7,
            "8": Day8,
            "9": Day9,
            "10": Day10,
            "11": Day11,
            "12": Day12,
            "13": Day13,
            "14": Day14,
            "15": Day15,
            "16": Day16,
            "17": Day17,
            "18": Day18,
            "19": Day19,
            "20": Day20,
            "21": Day21,
            "22": Day22,
            "23": Day23,
            "24": Day24,
            "25": Day25
        }

    def getSolution(self, day):
        return self.__solutionMap[day]()
