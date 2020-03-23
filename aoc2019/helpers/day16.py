from numpy import dot


def improveSignalQuality(signal, phases, charactersNeeded):
    result = [int(x) for x in str(signal)]

    for _ in range(phases):
        result = __runPhase(result)

    return __formatResult(result, charactersNeeded)


def __runPhase(signal):
    result = []

    for i in range(0, len(signal)):
        pattern = __getPattern(len(signal), i + 1)
        value = dot(signal, pattern)
        lastDigit = abs(value) % 10
        result.append(lastDigit)

    return result


def __getPattern(length, iteration):
    zeros = [0] * iteration
    positives = [1] * iteration
    negatives = [-1] * iteration
    pattern = zeros + positives + zeros + negatives

    while len(pattern) < length + 1:
        pattern = pattern + pattern

    # Remove first element per instructions
    pattern.pop(0)

    # Trim to be same length as signal
    return pattern[0:length]


def __formatResult(signal, charactersNeeded):
    result = "".join(map(str, signal))
    return result[:charactersNeeded]


'''
Had to look for hints on this one since every approach I was taking was way too slow.  
This solution is my implementation of the algorithm described here:
https://nbviewer.jupyter.org/github/mjpieters/adventofcode/blob/master/2019/Day%2016.ipynb
'''


def decodeRealSignal(signal, rounds, charactersNeeded, startingPosition):
    # Assume everything before offset would have 0 modifier, so we can just ignore it
    signalAfterOffset = [int(x) for x in str(signal)][startingPosition:]

    for _ in range(rounds):
        newSignal = []
        currentSum = 0
        for i in range(len(signalAfterOffset) - 1, -1, -1):
            currentSum += signalAfterOffset[i]
            newSignal.append(currentSum % 10)

        signalAfterOffset = newSignal[::-1]

    return __formatResult(signalAfterOffset, charactersNeeded)
