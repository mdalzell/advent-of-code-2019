
from aoc2019.shared.intcode import IntCode


def countBlockTiles(program):
    intcode = IntCode(program)
    intcode.run()

    blockCount = 0
    for i in range(2, len(intcode.output), 3):
        if intcode.output[i] is 2:
            blockCount = blockCount + 1

    return blockCount
