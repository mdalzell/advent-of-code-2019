class BfsSearchNode:
    def __init__(self, position, moves, parent = None, warpHistory = None):
        self.parent = parent
        self.position = position
        self.moves = moves
        self.warpHistory = warpHistory or []

def getMinimumSteps(maze, multilevel = False):
    startingPoint, endingPoint, warpPoints = _parseMaze(maze, multilevel)
    return _searchMaze(startingPoint, endingPoint, warpPoints, maze)

def _parseMaze(maze, multilevel):
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
        portal = portalDictionary[key][0]
        if key == "AA":
            startingPoint = (portal[0], portal[1], 0)
        elif key == "ZZ":
            endingPoint = (portal[0], portal[1], 0)
        else:
            warpPointEnd = portalDictionary[key][1]
            warpPoints[portal] = ((warpPointEnd[0], warpPointEnd[1], _determineLevelModifier(maze, portal, multilevel)), key)
            warpPoints[warpPointEnd] = ((portal[0], portal[1], _determineLevelModifier(maze, warpPointEnd, multilevel)), key)

    return startingPoint, endingPoint, warpPoints

def _searchMaze(startingPoint, endingPoint, warpPoints, maze):
    startNode = BfsSearchNode(startingPoint, 0)
    searchNodes = [startNode]
    visitedNodes = set(startNode.position)

    while len(searchNodes) > 0:
        currentNode = searchNodes.pop(0)
        if currentNode.position in visitedNodes:
            continue

        if currentNode.position == endingPoint:
            return currentNode.moves

        searchNodes += _generateSuccessors(currentNode, warpPoints, maze)
        visitedNodes.add(currentNode.position)

    return 0

def _generateSuccessors(node, warpPoints, maze):
    successors = []
    x = node.position[0]
    y = node.position[1]
    z = node.position[2]
    if (x, y) in warpPoints:
        warpPoint = warpPoints[(x, y)][0]
        warpPosition = (warpPoint[0], warpPoint[1], warpPoint[2] + z)
        if warpPosition != node.parent and warpPosition[2] >= 0:
            warpHistory = node.warpHistory + [warpPoints[(x, y)][1]+ ' ' + str(warpPoint[2]) + ' ' + str((x, y))]
            successors.append(_makeNode(warpPosition, node, warpHistory))

    
    positions = [
        (x, y + 1, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x - 1, y, z)
    ]

    for position in positions:
        if position == node.parent:
            continue
        elif maze[position[1]][position[0]] is ".":
            successors.append(_makeNode(position, node, node.warpHistory))

    return successors

def _makeNode(position, parent, warpHistory):
    return BfsSearchNode(position, parent.moves + 1, parent.position, warpHistory)

def _determineLevelModifier(maze, point, multlevel):
    if not multlevel:
        return 0

    x = point[0]
    y = point[1]
    width = len(maze[0])
    height = len(maze)
    if x == 2 or x == width - 3 or y == 2 or y == height - 3:
        return -1
    else:
        return 1