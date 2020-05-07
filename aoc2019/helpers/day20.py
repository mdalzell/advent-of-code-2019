class BfsSearchNode:
    def __init__(self, position, moves, parent = None):
        self.parent = parent
        self.position = position
        self.moves = moves

def getMinimumSteps(maze):
    startingPoint, endingPoint, warpPoints = _parseMaze(maze)
    return _searchMaze(startingPoint, endingPoint, warpPoints, maze)

def _parseMaze(maze):
    portalDictionary = {}
    warpPoints = {}
    startingPoint = None
    endingPoint = None

    for y in range(1, len(maze) - 1):
        for x in range(1, len(maze[y]) - 1):
            currentSpace = maze[y][x]
            if currentSpace.isalpha():
                portalKey = None
                portalPoint = None

                neighbors = [
                    (x, y - 1),
                    (x + 1, y),
                    (x, y + 1),
                    (x - 1, y)
                ]

                for neighbor in neighbors:
                    neighborValue = maze[neighbor[1]][neighbor[0]]
                    if neighborValue is '.':
                        portalPoint = neighbor
                        
                        if neighbor[0] > x:
                            portalKey = maze[y][x - 1] + currentSpace
                        elif neighbor[0] < x:
                            portalKey = currentSpace + maze[y][x + 1]
                        elif neighbor[1] > y:
                            portalKey = maze[y - 1][x] + currentSpace
                        elif neighbor[1] < y:
                            portalKey = currentSpace + maze[y + 1][x]

                if portalPoint is not None:
                    if portalKey in portalDictionary:
                        portalDictionary[portalKey].append(portalPoint)
                    else:
                        portalDictionary[portalKey] = [portalPoint]

    for key in portalDictionary.keys():
        if key == "AA":
            startingPoint = portalDictionary[key][0]
        elif key == "ZZ":
            endingPoint = portalDictionary[key][0]
        else:
            warpPointStart = portalDictionary[key][0]
            warpPointEnd = portalDictionary[key][1]
            warpPoints[warpPointStart] = warpPointEnd
            warpPoints[warpPointEnd] = warpPointStart

    return startingPoint, endingPoint, warpPoints

def _searchMaze(startingPoint, endingPoint, warpPoints, maze):
    startNode = BfsSearchNode(startingPoint, 0)
    searchNodes = [startNode]

    while len(searchNodes) > 0:
        currentNode = searchNodes.pop(0)

        if currentNode.position == endingPoint:
            return currentNode.moves

        searchNodes += _generateSuccessors(currentNode, warpPoints, maze)

    return 0

def _generateSuccessors(node, warpPoints, maze):
    successors = []
    if node.position in warpPoints:
        warpPosition = warpPoints[node.position]
        if warpPosition != node.parent:
            successors.append(_makeNode(warpPosition, node))

    x = node.position[0]
    y = node.position[1]
    positions = [
        (x, y + 1),
        (x + 1, y),
        (x, y - 1),
        (x - 1, y)
    ]

    for position in positions:
        if position == node.parent:
            continue
        elif maze[position[1]][position[0]] is ".":
            successors.append(_makeNode(position, node))

    return successors

def _makeNode(position, parent):
    return BfsSearchNode(position, parent.moves + 1, parent.position)