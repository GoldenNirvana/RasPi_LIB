import RPi.GPIO as IO


class Decoder(object):
    def __init__(self, portA, portB, portC):
        self.__portA = portA
        self.__portB = portB
        self.__portC = portC
        IO.setmode(IO.BOARD)
        IO.setup(portA, IO.OUT)
        IO.setup(portB, IO.OUT)
        IO.setup(portC, IO.OUT)
        IO.output(portA, 0)
        IO.output(portB, 0)
        IO.output(portC, 0)


    def enable(self, port):
        binaryPort = f'{port:03b}'
        IO.output(self.__portA, int(binaryPort[2]))
        IO.output(self.__portB, int(binaryPort[1]))
        IO.output(self.__portC, int(binaryPort[0]))
        
        
SPI_BUS = Decoder(21, 22, 23)


