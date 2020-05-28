import sys
from aoc2019.solutions.solutionFactory import SolutionFactory

if __name__ == '__main__':
    problemNumber = sys.argv[1].split("-")
    day = problemNumber[0]
    part = problemNumber[1]
    solutionFactory = SolutionFactory()

    solution = solutionFactory.getSolution(day)
    result = solution.part2() if part == "2" else solution.part1()
    if result is not None: print(result)
