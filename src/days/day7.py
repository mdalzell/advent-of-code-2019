from ..shared.intcode import intcode

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
                            resultA = intcode(intList.copy(), [ampA, 0])[0]
                            resultB = intcode(intList.copy(), [ampB, resultA])[0]
                            resultC = intcode(intList.copy(), [ampC, resultB])[0]
                            resultD = intcode(intList.copy(), [ampD, resultC])[0]
                            resultE = intcode(intList.copy(), [ampE, resultD])[0]
                            if resultE > maxSignal:
                                maxSignal = resultE

    return maxSignal