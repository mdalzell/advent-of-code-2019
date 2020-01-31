import sys


def buildImage(input, width, height):
    layers = []
    inputPointer = 0

    while inputPointer < len(input):
        layer = []
        for _ in range(0, height):
            layerRow = []
            for _ in range(0, width):
                layerRow.append(input[inputPointer])
                inputPointer += 1

            layer.append(layerRow)

        layers.append(layer)

    return layers


def getLayerWithFewestOfDigit(image, digitChar):
    maxCount = sys.maxsize
    bestLayer = None
    for layer in image:
        count = getCountOfDigitInLayer(layer, digitChar)
        if count < maxCount:
            bestLayer = layer
            maxCount = count

    return bestLayer


def getCountOfDigitInLayer(layer, digitChar):
    count = 0
    for row in layer:
        count += row.count(digitChar)

    return count


def combineLayers(image, width, height):
    flatImage = []
    for y in range(0, height):
        newRow = []
        for x in range(0, width):
            layerNumber = 0
            while layerNumber < len(image):
                val = image[layerNumber][y][x]
                if val != '2':
                    newRow.append(val)
                    break
                layerNumber += 1
        flatImage.append(newRow)

    return flatImage
