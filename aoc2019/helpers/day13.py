
from aoc2019.shared.intcode import IntCode


def countBlockTiles(program):
    intcode = IntCode(program)
    intcode.run()

    blockCount = 0
    for i in range(2, len(intcode.output), 3):
        if intcode.output[i] is 2:
            blockCount = blockCount + 1

    return blockCount


def getScore(program):
    intcode = IntCode(program)
    score = 0
    ballPos = None
    paddlePos = None

    while not intcode.finished:
        intcode.run()

        for i in range(0, len(intcode.output), 3):
            xPos = intcode.output[i]
            yPos = intcode.output[i + 1]
            tyleId = intcode.output[i + 2]

            if xPos is -1 and yPos is 0:
                score = tyleId
            elif tyleId == 4:
                ballPos = (xPos, yPos)
            elif tyleId == 3:
                paddlePos = (xPos, yPos)

        if ballPos[0] > paddlePos[0]:
            intcode.inputs.append(1)
        elif ballPos[0] < paddlePos[0]:
            intcode.inputs.append(-1)
        else:
            intcode.inputs.append(0)

        intcode.clearOutput()

    return score
