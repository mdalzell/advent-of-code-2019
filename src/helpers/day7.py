from ..shared.intcode import IntCode


def findMaxSignal(intList, begin, end):
    maxSignal = 0

    # Yo dawg I heard you like loops
    for ampA in range(begin, end):
        for ampB in range(begin, end):
            for ampC in range(begin, end):
                for ampD in range(begin, end):
                    for ampE in range(begin, end):
                        ampList = [ampA, ampB, ampC, ampD, ampE]
                        if len(set(ampList)) == len(ampList):
                            intCodeA = IntCode(intList.copy(), [ampA])
                            intCodeB = IntCode(intList.copy(), [ampB])
                            intCodeC = IntCode(intList.copy(), [ampC])
                            intCodeD = IntCode(intList.copy(), [ampD])
                            intCodeE = IntCode(intList.copy(), [ampE])
                            beginSignal = 0

                            while not intCodeE.finished:
                                intCodeA.inputs.append(beginSignal)
                                intCodeA.run()

                                intCodeB.inputs.append(intCodeA.output[-1])
                                intCodeB.run()

                                intCodeC.inputs.append(intCodeB.output[-1])
                                intCodeC.run()

                                intCodeD.inputs.append(intCodeC.output[-1])
                                intCodeD.run()

                                intCodeE.inputs.append(intCodeD.output[-1])
                                intCodeE.run()

                                beginSignal = intCodeE.output[-1]

                            if intCodeE.output[-1] > maxSignal:
                                maxSignal = intCodeE.output[-1]

    return maxSignal
