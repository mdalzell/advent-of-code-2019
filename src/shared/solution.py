import abc
import os

class Solution:
    def __init__(self):
        self.dirPath = os.path.dirname(os.path.abspath(__file__))
    @abc.abstractmethod
    def part1(self):
        pass
    @abc.abstractmethod
    def part2(self):
        pass
