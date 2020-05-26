__SEPARATOR = '/'

__LAYER_TEMPLATE = '...../...../..?../...../.....'

__INNER_BORDER = set([(1,2), (3,2), (2,1), (2,3)])

def calculateBiodiversityRating(layout):
    layoutString = layout.replace(__SEPARATOR, '')
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

def countBugsAfterMinutes(initialLayout, numberOfMinutes):
    layoutLevels = {}
    layoutLevels[0] = initialLayout
    maxLevel = 0
    minLevel = 0

    for _ in range(0, numberOfMinutes):
        # Add possible new levels
        maxLevel += 1
        minLevel -= 1
        layoutLevels[maxLevel] = __LAYER_TEMPLATE
        layoutLevels[minLevel] = __LAYER_TEMPLATE

        layoutLevels = __calculateNextLayoutRecursively(layoutLevels, minLevel, maxLevel)

        # Remove outside levels if no bugs
        if __countBugsInLayout(layoutLevels[maxLevel]) == 0:
            del layoutLevels[maxLevel]
            maxLevel -= 1
        
        if __countBugsInLayout(layoutLevels[minLevel]) == 0:
            del layoutLevels[minLevel]
            minLevel += 1

    totalBugs = 0
    for layerIndex in layoutLevels.keys():
        totalBugs += __countBugsInLayout(layoutLevels[layerIndex])

    return totalBugs

def __calculateNextLayout(currentLayout):
    currentLayoutMatrix = currentLayout.split(__SEPARATOR)
    columnLength, rowLength = __getDimensions(currentLayoutMatrix)

    nextLayoutMatrix = ['' * rowLength] * columnLength

    for y in range(0, columnLength):
        for x in range(0, rowLength):
            adjacentBugCount = __calculateAdjacentBugCountOnLevel(currentLayoutMatrix, rowLength, columnLength, x, y)
            currentSpace = currentLayoutMatrix[y][x]
            nextLayoutMatrix[y] += __getNextSpace(currentSpace, adjacentBugCount)

    return __SEPARATOR.join(nextLayoutMatrix)

def __calculateNextLayoutRecursively(layoutGrid, minLevel, maxLevel):
    newLayoutGrid = layoutGrid.copy()
    for layoutLevel in layoutGrid.keys():
        layout = layoutGrid[layoutLevel]
        currentLayoutMatrix = layout.split(__SEPARATOR)
        columnLength, rowLength = __getDimensions(currentLayoutMatrix)

        nextLayoutMatrix = ['' * rowLength] * columnLength

        for y in range(0, columnLength):
            for x in range(0, rowLength):
                adjacentBugCount = __calculateAdjacentBugCountOnLevel(currentLayoutMatrix, rowLength, columnLength, x, y)
                
                if (x, y) in __INNER_BORDER and layoutLevel != maxLevel:
                    adjacentBugCount += __calculateAdjacentBugCountFromInnerLevel(layoutGrid[layoutLevel + 1], x, y)
                
                if (x == 0 or x == 4 or y == 0 or y == 4) and layoutLevel != minLevel:
                    adjacentBugCount += __calculateAdjacentBugCountFromOuterLevel(layoutGrid[layoutLevel - 1], x, y)

                currentSpace = currentLayoutMatrix[y][x]
                nextLayoutMatrix[y] += __getNextSpace(currentSpace, adjacentBugCount)

        newLayoutGrid[layoutLevel] = __SEPARATOR.join(nextLayoutMatrix)

    return newLayoutGrid

def __calculateAdjacentBugCountOnLevel(currentLayoutMatrix, rowLength, columnLength, x, y):
    adjacentBugCount = 0

    if (x > 0 and currentLayoutMatrix[y][x - 1] == '#'): adjacentBugCount += 1 
    if (x < rowLength - 1 and currentLayoutMatrix[y][x + 1] == '#'): adjacentBugCount += 1
    if (y > 0 and currentLayoutMatrix[y - 1][x] == '#'): adjacentBugCount += 1
    if (y < columnLength - 1 and currentLayoutMatrix[y + 1][x] == '#'): adjacentBugCount += 1

    return adjacentBugCount

def __calculateAdjacentBugCountFromInnerLevel(innerLayout, x, y):
    adjacentBugCount = 0
    currentLayoutMatrix = innerLayout.split(__SEPARATOR)
    columnLength, rowLength = __getDimensions(currentLayoutMatrix)

    if (x,y) == (1,2):
        for i in range(0, columnLength):
            if currentLayoutMatrix[i][0] == '#':
                adjacentBugCount += 1
    elif (x,y) == (3,2):
        for i in range(0, columnLength):
            if currentLayoutMatrix[i][4] == '#':
                adjacentBugCount += 1
    elif (x,y) == (2,1):
        for i in range(0, rowLength):
            if currentLayoutMatrix[0][i] == '#':
                adjacentBugCount += 1
    elif (x,y) == (2,3):
        for i in range(0, rowLength):
            if currentLayoutMatrix[4][i] == '#':
                adjacentBugCount += 1

    return adjacentBugCount

def __calculateAdjacentBugCountFromOuterLevel(outerLayout, x, y):
    adjacentBugCount = 0
    outerMatrix = outerLayout.split(__SEPARATOR)

    if x == 0 and outerMatrix[2][1] == '#':
        adjacentBugCount += 1
    if x == 4 and outerMatrix[2][3] == '#':
        adjacentBugCount += 1
    if y == 0 and outerMatrix[1][2] == '#':
        adjacentBugCount += 1
    if y == 4 and outerMatrix[3][2] == '#':
        adjacentBugCount += 1

    return adjacentBugCount

def __getNextSpace(currentSpace, adjacentBugCount):
    if currentSpace == '#' and adjacentBugCount != 1:
        return '.'
    elif currentSpace == '.' and (adjacentBugCount == 1 or adjacentBugCount == 2):
        return '#'
    else:
        return currentSpace

def __getDimensions(matrix):
    return len(matrix), len(matrix[0])

def __countBugsInLayout(layoutString):
    return layoutString.count('#')
