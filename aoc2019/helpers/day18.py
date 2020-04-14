from functools import reduce

class SearchNode:
    def __init__(self, position, moves, keys):
        self.position = position
        self.moves = moves
        self.keys = keys
        self.priority = moves - len(keys)

    def __str__(self):
        return ('position: ' + str(self.position) 
        + ', moves: ' + str(self.moves) 
        + ', priority: ' + str(self.priority) 
        + ', keys: ' + str(self.keys))

def minimumStepsToCollectAllKeys(scanMap):
    startingNode, totalKeyCount = _getStartingNodeAndGoal(scanMap)
    searchResult = _aStarSearch(scanMap, startingNode, totalKeyCount)
    return searchResult.moves

def _aStarSearch(scanMap, startingNode, totalKeyCount):
    openList = []
    closedList = []

    openList.append(startingNode)

    while len(openList) is not 0:
        currentIndex = _bestPriorityIndex(openList)
        currentNode = openList.pop(currentIndex)
        successors = _generateSuccessors(currentNode, scanMap)

        # print(currentNode)

        for successor in successors:
            if len(successor.keys) is totalKeyCount:
                return successor

            if _isNodeVisited(successor, openList) or _isNodeVisited(successor, closedList):
                continue

            openList.append(successor)

        closedList.append(currentNode)

    return None

def _bestPriorityIndex(openList):
    bestPriorityIndex = 0
    for i in range(1, len(openList)):
        if openList[i].priority < openList[i-1].priority:
            bestPriorityIndex = i

    return bestPriorityIndex

def _getStartingNodeAndGoal(scanMap):
    totalKeyCount = 0
    startingNode = None

    for i in range(0, len(scanMap)):
        for j in range(0, len(scanMap[i])):
            character = scanMap[i][j]
            if character.islower():
                totalKeyCount += 1
            elif character is "@":
                startingNode = SearchNode((j, i), 0, [])

    return startingNode, totalKeyCount

def _generateSuccessors(currentNode, scanMap):
    successors = []
    successorPositions = [
        (currentNode.position[0] + 1, currentNode.position[1]),
        (currentNode.position[0] - 1, currentNode.position[1]),
        (currentNode.position[0], currentNode.position[1] + 1),
        (currentNode.position[0], currentNode.position[1] - 1)
    ]

    for position in successorPositions:
        character = scanMap[position[1]][position[0]]
        
        if character is '#':
            continue
        elif character.isupper():
            if character.lower() in currentNode.keys:
                successor = SearchNode(position, currentNode.moves + 1, currentNode.keys)
                successors.append(successor)
            else:
                continue
        elif character.islower() and character not in currentNode.keys:
            newKeys = currentNode.keys + [character]
            successor = SearchNode(position, currentNode.moves + 1, newKeys)
            successors.append(successor)
        else:
            successor = SearchNode(position, currentNode.moves + 1, currentNode.keys)
            successors.append(successor)

    return successors

def _isNodeVisited(currentNode, nodeList):
    for node in nodeList:
        if (node.position == currentNode.position
        and node.moves <= currentNode.moves
        and set(node.keys) == set(currentNode.keys)):
            return True

    return False