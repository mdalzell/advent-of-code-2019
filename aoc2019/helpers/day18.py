from functools import reduce
from queue import PriorityQueue

class SearchNode:
    def __init__(self, positions, moves, keys, keyDictionary):
        self.positions = positions
        self.moves = moves
        self.keys = keys
        self.maxDistanceToKey = _maxDistanceToKey(positions, keys, keyDictionary)
        self.priority = moves + self.maxDistanceToKey

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

    for line in scanMap:
        print(line)
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
        successors = _generateSuccessors(currentNode, scanMap, keyLocations)

        for successor in successors:
            if len(successor.keys) is len(keyLocations):
                return successor

            successorDictionaryKey = _buildKey(successor)

            if successorDictionaryKey in visitedNodes.keys() and successor.priority >= visitedNodes[successorDictionaryKey]:
                continue

            openQueue.put(successor)
        
        dictionaryKey = _buildKey(currentNode)
        visitedNodes[dictionaryKey] = currentNode.priority
        openQueue.task_done()

    return None

def _getStartingPositionsAndKeyLocations(scanMap):
    keyLocations = {}
    startingPostions = []

    for i in range(0, len(scanMap)):
        for j in range(0, len(scanMap[i])):
            character = scanMap[i][j]
            if character.islower():
                keyLocations[character] = (j, i)
            elif character is "@":
                startingPostions.append((j, i))

    startingNodes = SearchNode(startingPostions, 0, '', keyLocations)
    return startingNodes, keyLocations

def _generateSuccessors(currentNode, scanMap, keyLocations):
    successors = []

    for i in range(0, len(currentNode.positions)):
        successorPositions = [
            (currentNode.positions[i][0] + 1, currentNode.positions[i][1]),
            (currentNode.positions[i][0] - 1, currentNode.positions[i][1]),
            (currentNode.positions[i][0], currentNode.positions[i][1] + 1),
            (currentNode.positions[i][0], currentNode.positions[i][1] - 1)
        ]

        for position in successorPositions:
            character = scanMap[position[1]][position[0]]
            
            if character is '#':
                continue
            elif character.isupper():
                if character.lower() in currentNode.keys:
                    updatedPositions = currentNode.positions.copy()
                    updatedPositions[i] = position
                    successor = SearchNode(updatedPositions, currentNode.moves + 1, currentNode.keys, keyLocations)
                    successors.append(successor)
                else:
                    continue
            elif character.islower() and character not in currentNode.keys:
                newKeys = ''.join(sorted(currentNode.keys + character))
                updatedPositions = currentNode.positions.copy()
                updatedPositions[i] = position
                successor = SearchNode(updatedPositions, currentNode.moves + 1, newKeys, keyLocations)
                successors.append(successor)
            else:
                updatedPositions = currentNode.positions.copy()
                updatedPositions[i] = position
                successor = SearchNode(updatedPositions, currentNode.moves + 1, currentNode.keys, keyLocations)
                successors.append(successor)

    return successors

def _maxDistanceToKey(positions, keys, keyLocations):
    maxDistance = 0

    for position in positions:
        for character in keyLocations.keys():
            if character not in keys:
                distance = abs(position[0] - keyLocations[character][0]) + abs(position[1] - keyLocations[character][1])
                if distance > maxDistance:
                    maxDistance = distance

    return maxDistance

def _buildKey(node):
    key = str(node.positions) + node.keys
    return key