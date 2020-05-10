from aoc2019.shared.intcode import IntCode

class SpringBot:
    def __init__(self, program):
        self.__computer = IntCode(program)

    def loadSpringScript(self, commands):
        asciiValues = []

        for command in commands:
            for character in command:
                asciiValues.append(ord(character))

            asciiValues.append(10)

        self.__computer.inputs += asciiValues

    def run(self):
        self.__computer.run()
        if self.__computer.output[-1] > 128:
            return self.__computer.output[-1]

        printString = ""
        for output in self.__computer.output:
            printString += chr(output)
        
        print(printString)

testSpringCommands = ['OR A T', 'AND B T', 'AND C T', 'NOT T T', 'AND D T', 'OR T J', 'WALK']