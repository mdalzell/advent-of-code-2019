class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

def buildTree(orbitDictionary, rootValue):
    rootNode = Node(rootValue)

    if rootValue in orbitDictionary:
        childList = orbitDictionary[rootNode.value]

        for child in childList:
            childNode = buildTree(orbitDictionary, child)
            childNode.parent = rootNode
            rootNode.children.append(childNode)

    return rootNode

def buildOrbitDictionary(orbitMap):
    dictionary = {}
    for orbit in orbitMap:
        [centerOfMass, satellite] = orbit.split(')')

        if centerOfMass in dictionary:
            dictionary[centerOfMass].append(satellite)
        else:
            dictionary[centerOfMass] = [satellite]

    return dictionary

def getOrbits(tree, level):
    orbitSum = 0

    for child in tree.children:
        orbitSum += getOrbits(child, level + 1)

    return orbitSum + level

def calculateNumberOfOrbits(orbitMap):
    dictionary = buildOrbitDictionary(orbitMap)
    tree = buildTree(dictionary, "COM")
    return getOrbits(tree, 0)

def findLocation(orbitTree, value):
    if orbitTree.value == value:
        return orbitTree
    else:
        foundNode = None
        for child in orbitTree.children:
            foundNode = findLocation(child, value)
            if foundNode is not None:
                return foundNode
        
        return None

def reorientTree(rootNode, parent):
    if rootNode.parent is not None:
        reorientTree(rootNode.parent, rootNode)
        rootNode.children.append(rootNode.parent)
        
    if parent is not None:
        rootNode.children.remove(parent)
    
    rootNode.parent = parent  
    
    return rootNode

def findNodeDistance(rootNode, value, level):
    if rootNode.value == value:
        return level - 2 # Not counting orbits either that I or Santa am in
    
    foundDistance = 0
    for child in rootNode.children:
        foundDistance = findNodeDistance(child, value, level + 1)
        if foundDistance is not 0:
            break
        
    return foundDistance
        

def getToSanta(orbitMap):
    dictionary = buildOrbitDictionary(orbitMap)
    tree = buildTree(dictionary, "COM")

    currentLocation = findLocation(tree, "YOU")
    reorientedTree = reorientTree(currentLocation, None)
    return findNodeDistance(reorientedTree, "SAN", 0) 
    