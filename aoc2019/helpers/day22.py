_DEAL_WITH_INCREMENT = "deal with increment"

_CUT = "cut "

def shuffleNewDeck(deckSize, instructions):
    deck = list(range(0, deckSize))

    for instruction in instructions:
        if _DEAL_WITH_INCREMENT in instruction:
            increment = _getInstructionValue(instruction)
            deck = _dealWithIncrement(deck, increment)
        elif _CUT in instruction:
            cut = _getInstructionValue(instruction)
            deck = _cutDeck(deck, cut)
        else:
            _dealIntoNewStack(deck)

    return deck

def _getInstructionValue(instruction):
    return int(instruction.split(' ')[-1])

def _dealIntoNewStack(deck):
    deck.reverse()

def _cutDeck(deck, number):
    return  deck[number:] + deck[:number]
    
def _dealWithIncrement(deck, increment):
    currentIndex = 0
    newDeck = [None] * len(deck)

    while len(deck) > 0:
        currentCard = deck.pop(0)
        newDeck[currentIndex] = currentCard

        currentIndex += increment

        if currentIndex > len(newDeck) - 1:
            currentIndex = currentIndex - len(newDeck)

    return newDeck

# Didn't really understand the modular math required to solve this problem.
# Luckily found some good tips on reddit that helped explain how to do this
# Each shuffle action can be represented as a linear operation , which can then be combined to get a single equation increment * x + offset
# https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
def superShuffle(deckSize, instructions, numberOfShuffles, cardToPick):
    incrementMultiplier = 1
    offsetMultiplier = 0

    for instruction in instructions:
        if _DEAL_WITH_INCREMENT in instruction:
            value = _getInstructionValue(instruction)
            incrementMultiplier *= _modularInverse(value, deckSize)
            incrementMultiplier %= deckSize
        elif _CUT in instruction:
            value = _getInstructionValue(instruction)
            offsetMultiplier += value * incrementMultiplier
            offsetMultiplier %= deckSize
        else:
            incrementMultiplier *= -1
            incrementMultiplier %= deckSize

            offsetMultiplier += incrementMultiplier
            offsetMultiplier %= deckSize

    increment = pow(incrementMultiplier, numberOfShuffles, deckSize)
    offset = offsetMultiplier * (1 - increment) * _modularInverse((1 - incrementMultiplier) % deckSize, deckSize)
    offset %= deckSize

    return (offset + cardToPick * increment) % deckSize

def _modularInverse(n, mod):
    return pow(n, mod - 2, mod)