from aoc2019.shared.intcode import IntCode

class NetworkComputer:
    def __init__(self, program, id):
        self.__computer = IntCode(program, [id])
        self.__queue = []

    def __getNextPacket(self):
        if len(self.__queue) is 0:
            return [-1]
        else:
            packet = self.__queue.pop(0)
            return [packet.x, packet.y]

    def processRequests(self):
        outgoingPackets = []
        packet = self.__getNextPacket()
        self.__computer.inputs = self.__computer.inputs + packet
        self.__computer.run()

        for i in range(0, len(self.__computer.output), 3):
            destination = self.__computer.output[i]
            x = self.__computer.output[i + 1]
            y = self.__computer.output[i + 2]
            packet = Packet(destination, x, y)
            outgoingPackets.append(packet)

        self.__computer.clearOutput()
        return outgoingPackets

    def addPacketToQueue(self, packet):
        self.__queue.append(packet)

class Packet:
    def __init__(self, destination, x, y):
        self.destination = destination
        self.x = x
        self.y = y

def buildNetwork(program):
    network = {}
    for i in range(0, 50):
        network[i] = NetworkComputer(program, i)

    return network

def findFirstPacketToAddress(network, address):
    while True:
        for id in network.keys():
            computer = network[id]
            outgoingPackets = computer.processRequests()

            for packet in outgoingPackets:
                if packet.destination == address:
                    return packet
                else:
                    network[packet.destination].addPacketToQueue(packet)
