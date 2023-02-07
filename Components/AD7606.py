from Config.Spi import progSpi, appSpi, decoder
import RPi.GPIO as IO
import serial

class Ad7606:
    def __init__(self, port):
        self.__port = port
        self.__ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.__decoder = decoder
        self.__spi = appSpi
        IO.setwarnings(False)
        IO.setmode(IO.BOARD)
        self.__busy = 38
        self.__conv = 32
        IO.setup(self.__busy, IO.IN)
        IO.setup(self.__conv, IO.OUT)
        IO.output(self.__conv, 1)

    def doSettings(self):
        self.__spi.mode = 2

    def readByAppSpi(self):
        #self.__decoder.enable(self.__port)
        #self.doSettings()

        while True:
            if self.__ser.in_waiting > 0:
                line = self.__ser.readline().decode('utf-8').rstrip()
                return line


