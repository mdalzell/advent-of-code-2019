from aoc2019.shared.intcode import IntCode

class RescueBot:
    def __init__(self, program):
        self.__computer = IntCode(program)


    def beginSearch(self):
        while not self.__computer.finished:
            self.__computer.run()

            self.__printOutput()

            if self.__computer.requiresInput:
                command = input('Please enter command: ')
                if command == 'quit':
                    return
                else:
                    self.__computer.inputs += self.__stringToAsciiArray(command)

        self.__printOutput()

    def __stringToAsciiArray(self, command):
        return [ord(i) for i in list(command)] + [10]

    def __printOutput(self):
        print(''.join([chr(i) for i in self.__computer.output]))
        self.__computer.clearOutput()


