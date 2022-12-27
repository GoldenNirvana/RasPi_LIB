from Config.Spi import spi

class Pot:
    def __init__(self, port, gain=None):
        self.__spi = spi
        self.__gain = 128
        if gain is not None:
            self.__gain = gain
        self.__port = port
        
        
    def setGain(self, gain):
        self.__gain = gain
        self.__spi.send10(self.__gain, self.__port)