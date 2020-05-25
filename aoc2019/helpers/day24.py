__SEPERATOR = '/'

def calculateBiodiversityRating(layout):
    layoutString = layout.replace(__SEPERATOR, '')
    biodiveristyRating = 0
    for i in range(0, len(layoutString)):
        if layoutString[i] == '#':
            biodiveristyRating += pow(2, i)

    return biodiveristyRating

def getFirstLayoutToAppearTwice(layout):
    allLayouts = set()
    allLayouts.add(layout)
    currentLayout = layout
    
    while True:
        nextLayout = __calculateNextLayout(currentLayout)

        if nextLayout in allLayouts:
            return nextLayout
        else:
            allLayouts.add(nextLayout)
            currentLayout = nextLayout

def __calculateNextLayout(currentLayout):
    currentLayoutMatrix = currentLayout.split(__SEPERATOR)
    columnLength = len(currentLayoutMatrix)
    rowLength = len(currentLayoutMatrix[0])

    nextLayoutMatrix = ['' * rowLength] * columnLength

    for j in range(0, columnLength):
        for i in range(0, rowLength):
            adjacentBugCount = 0

            if (i > 0 and currentLayoutMatrix[j][i - 1] == '#'): adjacentBugCount += 1 
            if (i < rowLength - 1 and currentLayoutMatrix[j][i + 1] == '#'): adjacentBugCount += 1
            if (j > 0 and currentLayoutMatrix[j - 1][i] == '#'): adjacentBugCount += 1
            if (j < columnLength - 1 and currentLayoutMatrix[j + 1][i] == '#'): adjacentBugCount += 1

            currentSpace = currentLayoutMatrix[j][i]
            nextSpace = None
            if currentSpace == '#' and adjacentBugCount != 1:
                nextSpace = '.'
            elif currentSpace == '.' and (adjacentBugCount == 1 or adjacentBugCount == 2):
                nextSpace = '#'
            else:
                nextSpace = currentSpace

            nextLayoutMatrix[j] += nextSpace

    return __SEPERATOR.join(nextLayoutMatrix)