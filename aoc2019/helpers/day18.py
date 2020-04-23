from functools import reduce
from queue import PriorityQueue

class SearchNode:
    def __init__(self, positions, moves, keys):
        self.positions = positions
        self.moves = moves
        self.keys = keys
        self.priority = moves 

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return ('positions: ' + str(self.positions) 
        + ', moves: ' + str(self.moves) 
        + ', priority: ' + str(self.priority) 
        + ', keys: ' + str(self.keys))

def correctMapData(scanMap):
    for i in range(0, len(scanMap)):
        if "@" in scanMap[i]:
            index = scanMap[i].index("@")

            previousRow = list(scanMap[i - 1])
            previousRow[index - 1] = "@"
            previousRow[index] = "#"
            previousRow[index + 1] = "@"
            scanMap[i - 1] = "".join(previousRow)

            currentRow = list(scanMap[i])
            currentRow[index - 1] = "#"
            currentRow[index] = "#"
            currentRow[index + 1] = "#"
            scanMap[i] = "".join(currentRow)

            nextRow = list(scanMap[i + 1])
            nextRow[index - 1] = "@"
            nextRow[index] = "#"
            nextRow[index + 1] = "@"
            scanMap[i + 1] = "".join(nextRow)

            break
        else: 
            continue

    return scanMap

def minimumStepsToCollectAllKeys(scanMap):
    startingPositions, keyLocations = _getStartingPositionsAndKeyLocations(scanMap)
    searchResult = _search(scanMap, startingPositions, keyLocations)
    return searchResult.moves

def _search(scanMap, startingNode, keyLocations):
    openList = []
    visitedNodes = {}
    openQueue = PriorityQueue()
    openQueue.put(startingNode)

    openList.append(startingNode)

    while not openQueue.empty():
        currentNode = openQueue.get()
        dictionaryKey = _buildKey(currentNode)

        if len(currentNode.keys) is len(keyLocations):
            return currentNode

        if dictionaryKey in visitedNodes.keys() and currentNode.priority >= visitedNodes[dictionaryKey]:
            openQueue.task_done()
            continue

        successors = _generateSuccessors(currentNode, scanMap)

        for successor in successors:
            openQueue.put(successor)
        
        dictionaryKey = _buildKey(currentNode)
        visitedNodes[dictionaryKey] = currentNode.priority
        openQueue.task_done()

    return None

def _getStartingPositionsAndKeyLocations(scanMap):
    keyLocations = {}
    startingPositions = []

    for i in range(0, len(scanMap)):
        for j in range(0, len(scanMap[i])):
            character = scanMap[i][j]
            if character.islower():
                keyLocations[character] = (j, i)
            elif character is "@":
                startingPositions.append((j, i))

    startingNodes = SearchNode(startingPositions, 0, '')
    return startingNodes, keyLocations

def _generateSuccessors(currentNode, scanMap):
    successors = []

    for i in range(0, len(currentNode.positions)):
        queue = [(currentNode.positions[i], currentNode.moves)]
        visitedPositions = set()

        while len(queue) > 0:
            pathNode = queue.pop(0)
            pathPosition = pathNode[0]
            moves = pathNode[1]

            successorPositions = [
                (pathPosition[0] + 1, pathPosition[1]),
                (pathPosition[0] - 1, pathPosition[1]),
                (pathPosition[0], pathPosition[1] + 1),
                (pathPosition[0], pathPosition[1] - 1)
            ]

            for position in successorPositions:
                if position in visitedPositions:
                    continue

                character = scanMap[position[1]][position[0]]
                
                if character is '#' or (character.isupper() and character.lower() not in currentNode.keys):
                    continue
                elif character.islower() and character not in currentNode.keys:
                    newKeys = ''.join(sorted(currentNode.keys + character))
                    updatedPositions = currentNode.positions.copy()
                    updatedPositions[i] = position
                    successor = SearchNode(updatedPositions, moves + 1, newKeys)
                    successors.append(successor)

                queue.append((position, moves + 1))

            visitedPositions.add(pathPosition)

    return successors

def _buildKey(node):
    key = str(node.positions) + node.keys
    return key