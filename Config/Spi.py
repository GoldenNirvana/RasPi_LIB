import RPi.GPIO as IO
import gpiozero
import time


class Decoder(object):
    def __init__(self, portA, portB, portC):
        self.__portA = portA
        self.__portB = portB
        self.__portC = portC
        IO.setwarnings(False)
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
        

decoder = Decoder(7, 11, 15)


class Spi(object):
    def __init__(self):
        self.dec = decoder
        self.dataPin = gpiozero.OutputDevice(pin = 26)
        self.clkPin = gpiozero.OutputDevice(pin = 19)
        self.fsyncPin = gpiozero.OutputDevice(pin = 6)
        self.miso = 13
        IO.setup(self.miso, IO.IN)
        self.fsyncPin.on()
        self.clkPin.on()
        self.dataPin.off()
    

    def send16(self, n, cs):
        decoder.enable(cs)
        word = ''
        self.fsyncPin.off()
        values = [0x0,0x0]
        mask = 1 << 15
        for i in range(0, 16):
            self.dataPin.value = bool(n & mask)
            self.clkPin.off()
            self.clkPin.on()
            bit = IO.input(self.miso)
            word = word + str(bit)
            mask = mask >> 1
            if i == 7:
                values[0] = int(word, 2)
                word = ''
            if i == 15:
                values[1] = int(word, 2)
                word = ''
        self.dataPin.off()
        self.fsyncPin.on()
        return values
    
    
    def send8(self, n, cs):
        decoder.enable(cs)
        word = ''
        self.fsyncPin.off()
        values = [0x0]
        mask = 1 << 7
        for i in range(0, 8):
            self.dataPin.value = bool(n & mask)
            self.clkPin.off()
            self.clkPin.on()
            bit = IO.input(self.miso)
            word = word + str(bit)
            mask = mask >> 1
            if i == 7:
                values[0] = int(word, 2)
        self.dataPin.off()
        self.fsyncPin.on()
        return values
    
    def send10(self, n, cs):
        decoder.enable(cs)
        self.fsyncPin.off()
        self.dataPin.off()
        self.clkPin.on()
        self.clkPin.off()
        self.clkPin.on()
        self.clkPin.off()
        mask = 1 << 7
        for i in range(0, 8):
            self.dataPin.value = bool(n & mask)
            self.clkPin.on()
            self.clkPin.off()
            bit = IO.input(self.miso)
            mask = mask >> 1
        self.dataPin.off()
        self.fsyncPin.on()
        


spi = Spi()

