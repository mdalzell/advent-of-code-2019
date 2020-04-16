from functools import reduce
import queue

class SearchNode:
    def __init__(self, position, moves, keys, keyDictionary):
        self.position = position
        self.moves = moves
        self.keys = keys
        self.maxDistanceToKey = _maxDistanceToKey(position, keys, keyDictionary)
        self.priority = moves + self.maxDistanceToKey

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return ('position: ' + str(self.position) 
        + ', moves: ' + str(self.moves) 
        + ', priority: ' + str(self.priority) 
        + ', keys: ' + str(self.keys))

def minimumStepsToCollectAllKeys(scanMap):
    startingNode, keyLocations = _getStartingNodeAndKeyLocations(scanMap)
    searchResult = _aStarSearch(scanMap, startingNode, keyLocations)
    return searchResult.moves

def _aStarSearch(scanMap, startingNode, keyLocations):
    openList = []
    visitedNodes = {}
    openQueue = queue.PriorityQueue()
    openQueue.put(startingNode)

    openList.append(startingNode)

    while not openQueue.empty():
        currentNode = openQueue.get()
        successors = _generateSuccessors(currentNode, scanMap, keyLocations)

        for successor in successors:
            if len(successor.keys) is len(keyLocations):
                return successor

            successorDictionaryKey = (successor.position[0], successor.position[1], successor.keys)

            if successorDictionaryKey in visitedNodes.keys() and successor.priority >= visitedNodes[successorDictionaryKey]:
                continue

            openQueue.put(successor)
        
        dictionaryKey = (currentNode.position[0], currentNode.position[1], currentNode.keys)
        visitedNodes[dictionaryKey] = currentNode.priority
        openQueue.task_done()

    return None
    
def _getStartingNodeAndKeyLocations(scanMap):
    keyLocations = {}
    startingPostion = None

    for i in range(0, len(scanMap)):
        for j in range(0, len(scanMap[i])):
            character = scanMap[i][j]
            if character.islower():
                keyLocations[character] = (j, i)
            elif character is "@":
                startingPostion = (j, i)

    startingNode = SearchNode(startingPostion, 0, '', keyLocations)
    return startingNode, keyLocations

def _generateSuccessors(currentNode, scanMap, keyLocations):
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
                successor = SearchNode(position, currentNode.moves + 1, currentNode.keys, keyLocations)
                successors.append(successor)
            else:
                continue
        elif character.islower() and character not in currentNode.keys:
            newKeys = ''.join(sorted(currentNode.keys + character))
            successor = SearchNode(position, currentNode.moves + 1, newKeys, keyLocations)
            successors.append(successor)
        else:
            successor = SearchNode(position, currentNode.moves + 1, currentNode.keys, keyLocations)
            successors.append(successor)

    return successors

def _maxDistanceToKey(position, keys, keyLocations):
    maxDistance = 0

    for character in keyLocations.keys():
        if character not in keys:
            distance = abs(position[0] - keyLocations[character][0]) + abs(position[1] - keyLocations[character][1])
            if distance > maxDistance:
                maxDistance = distance

    return maxDistance