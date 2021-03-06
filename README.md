# Advent of Code 2019

This repository contains my solutions to the Advent of Code 2019 problems, implemented in Python3. It is also my first real attempt at working with Python for something beyond simple scripts.

For more information Advent of Code, check out the [site](https://adventofcode.com/2019), it's pretty cool :santa:

## Run Run Rudolph

To compute the solution to an Advent of Code problem, run the main script from the project's root directory:

```bash
$ python3 -m aoc2019 1-1
```

The argument `1-1` represents the day and the part(1 or 2) of the problem. For example, to get the answer for part two of day 4's problem, then the argument would be `4-2`.

## God Test Ye Merry Gentlemen

To run the tests, simply run this command from the project's root directory:

```bash
$ python3 -m unittest
```
The tests consist of unit tests of the helpers and solution tests, which use the real input from the problem.  A few of the solution tests are set to skip, since they take a while to run.
