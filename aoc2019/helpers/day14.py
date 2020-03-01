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


def calculateOreRequiredForFuel(formulaDictionary):
    currentIngredients = {'FUEL': 1, 'ORE': 0}
    continueRefining = True

    while continueRefining:
        continueRefining = False
        for key, value in currentIngredients.copy().items():
            if key != 'ORE' and value > 0:
                continueRefining = True
                formula = formulaDictionary[key]
                __refineIngredients(currentIngredients, formula)

    return currentIngredients['ORE']


def __refineIngredients(currentIngredients, formula):
    while currentIngredients[formula.element] > 0:
        for ingredient in formula.ingredients:
            __addIngredient(currentIngredients, ingredient)

        currentIngredients[formula.element] = currentIngredients[formula.element] - formula.count


def __addIngredient(currentIngredients, ingredient):
    ingredientElement = ingredient[1]
    ingredientCount = ingredient[0]
    if ingredientElement in currentIngredients:
        currentIngredients[ingredientElement] = currentIngredients[ingredientElement] + ingredientCount
    else:
        currentIngredients[ingredientElement] = ingredientCount
