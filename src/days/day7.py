from ..shared.intcode import IntCode

def findMaxSignal(intList):
    maxSignal = 0
    
    # Yo dawg I heard you like loops
    for ampA in range(0, 5):
        for ampB in range(0, 5):
            for ampC in range(0, 5):
                for ampD in range(0, 5):
                    for ampE in range(0, 5):
                        ampList = [ampA, ampB, ampC, ampD, ampE]
                        if len(set(ampList)) == len(ampList):
                            intcodeA = IntCode(intList.copy(), [ampA, 0])
                            intcodeA.run()

                            intcodeB = IntCode(intList.copy(), [ampB, intcodeA.output[-1]])
                            intcodeB.run()

                            intcodeC = IntCode(intList.copy(), [ampC, intcodeB.output[-1]])
                            intcodeC.run()

                            intcodeD = IntCode(intList.copy(), [ampD, intcodeC.output[-1]])
                            intcodeD.run()

                            intcodeE = IntCode(intList.copy(), [ampE, intcodeD.output[-1]])
                            intcodeE.run()

                            if intcodeE.output[-1] > maxSignal:
                                maxSignal = intcodeE.output[-1]

    return maxSignal