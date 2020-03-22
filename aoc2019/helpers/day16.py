from numpy import dot


def improveSignalQuality(signal, phases, charactersNeeded, startingPosition=0):
    result = [int(x) for x in str(signal)]

    for _ in range(phases):
        result = __runPhase(result)

    resultString = "".join(map(str, result))
    return resultString[startingPosition:charactersNeeded]


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
