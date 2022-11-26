import RPi.GPIO as IO


class Decoder(object):
    def __init__(self, portA, portB, portC, g1, g2a, g2b):
        self.__portA = portA
        self.__portB = portB
        self.__portC = portC
        self.__g1 = g1
        self.__g2a = g2a
        self.__g2b = g2b
        IO.setmode(IO.BOARD)
        IO.setup(portA, IO.OUT)
        IO.setup(portB, IO.OUT)
        IO.setup(portC, IO.OUT)
        IO.setup(g1, IO.OUT)
        IO.setup(g2a, IO.OUT)
        IO.setup(g2b, IO.OUT)
        IO.output(portA, 0)
        IO.output(portB, 0)
        IO.output(portC, 0)
        IO.output(g1, 0)
        IO.output(g2a, 0)
        IO.output(g2b, 0)

    def setPort(self, port):
        binaryPort = f'{port:03b}'
        IO.output(self.__portA, int(binaryPort[2]))
        IO.output(self.__portB, int(binaryPort[1]))
        IO.output(self.__portC, int(binaryPort[0]))
        IO.output(self.__g1, 1)
