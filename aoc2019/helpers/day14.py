import math


class Formula:
    def __init__(self, count, element, ingredients):
        self.count = count
        self.element = element
        self.ingredients = ingredients


def parseInputToFormulaDictionary(input):
    formulaDictionary = {}
    for line in input:
        line = line.strip()
        formulaParts = line.split('=>')
        formulaInputs = formulaParts[0].split(',')
        formulaOutput = formulaParts[1].strip().split(' ')

        ingredients = []
        for formulaInput in formulaInputs:
            formulaInputComponents = formulaInput.strip().split(' ')
            ingredient = (
                int(formulaInputComponents[0]), formulaInputComponents[1])
            ingredients.append(ingredient)

        formula = Formula(int(formulaOutput[0]), formulaOutput[1], ingredients)
        formulaDictionary[formula.element] = formula

    return formulaDictionary


def calculateOreRequiredForFuel(formulaDictionary, initialFuel=1):
    currentIngredients = {'FUEL': initialFuel, 'ORE': 0}
    continueRefining = True

    while continueRefining:
        continueRefining = False
        for key, value in currentIngredients.copy().items():
            if key != 'ORE' and value > 0:
                continueRefining = True
                formula = formulaDictionary[key]
                __refineIngredients(currentIngredients, formula)

    return currentIngredients['ORE']


def calculateMaxFuelForOre(formulaDictionary, oreCount=1000000000000):
    oreForOneFuel = calculateOreRequiredForFuel(formulaDictionary)
    minFuel = math.floor(oreCount / oreForOneFuel)
    # Just going to assume the leftovers will not allow more than 2x the min fuel that can be created
    maxFuel = minFuel * 2
    return __binarySearchForMaxFuel(formulaDictionary, minFuel, maxFuel, oreCount)


def __refineIngredients(currentIngredients, formula):
    multiplier = math.ceil(currentIngredients[formula.element] / formula.count)

    for ingredient in formula.ingredients:
        __addIngredient(currentIngredients, ingredient, multiplier)

    currentIngredients[formula.element] = currentIngredients[formula.element] - \
        formula.count * multiplier


def __addIngredient(currentIngredients, ingredient, multiplier):
    ingredientElement = ingredient[1]
    ingredientCount = ingredient[0]
    if ingredientElement in currentIngredients:
        currentIngredients[ingredientElement] = currentIngredients[ingredientElement] + \
            ingredientCount * multiplier
    else:
        currentIngredients[ingredientElement] = ingredientCount * multiplier


def __binarySearchForMaxFuel(formulaDictionary, minFuel, maxFuel, oreCount):
    if minFuel == (maxFuel - 1):
        # Take the lesser of the two binary search results
        return minFuel

    averageFuel = math.floor((minFuel + maxFuel) / 2)
    oreRequired = calculateOreRequiredForFuel(formulaDictionary, averageFuel)

    if oreRequired > oreCount:
        return __binarySearchForMaxFuel(formulaDictionary, minFuel, averageFuel, oreCount)
    elif oreRequired < oreCount:
        return __binarySearchForMaxFuel(formulaDictionary, averageFuel, maxFuel, oreCount)
