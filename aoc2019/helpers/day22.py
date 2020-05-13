def shuffleNewDeck(deckSize, instructions):
    deck = list(range(0, deckSize))

    for instruction in instructions:
        if "deal with increment" in instruction:
            increment = int(instruction.split(' ')[-1])
            deck = _dealWithIncrement(deck, increment)
        elif "cut" in instruction:
            cut = int(instruction.split(' ')[-1])
            deck = _cutDeck(deck, cut)
        else:
            _dealIntoNewStack(deck)

    return deck


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