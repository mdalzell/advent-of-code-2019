from aoc2019.shared.intcode import IntCode

def countAffectedPoints(program):
    points = 0
    computer = IntCode(program)

    for x in range(0, 50):
        for y in range(0, 50):
            computer.inputs = computer.inputs + [x, y]
            computer.run()
            output = computer.output[-1]

            if output is 1:
                points += 1

            computer.reset()

    return points

def getClosestEmitter(program):
    pass