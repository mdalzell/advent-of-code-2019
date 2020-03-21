

def improveSignalQuality(signal, phases, charactersNeeded):
    result = signal

    for _ in range(phases):
        result = __runPhase(result)

    return result[0:8]


def __runPhase(signal):
    result = ""

    for i in range(0, len(signal)):
        value = 0
        signalIndex = 0
        pattern = [0, 1, 0, -1]
        hasSkipped = False

        while signalIndex < len(signal):
            currentModifier = pattern.pop(0)
            for _ in range(i + 1):
                if signalIndex >= len(signal):
                    break

                if not hasSkipped:
                    hasSkipped = True
                    continue

                value += int(signal[signalIndex]) * currentModifier
                signalIndex += 1

            pattern.append(currentModifier)

        result += str(value)[-1]

    return result
