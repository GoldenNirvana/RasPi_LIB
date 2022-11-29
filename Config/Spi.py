import RPi.GPIO as IO
import gpiozero


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
        

decoder = Decoder(21, 22, 23)


class Spi(object):
    def __init__(self):
        self.dec = decoder
        self.dataPin = gpiozero.OutputDevice(pin = 10)
        self.clkPin = gpiozero.OutputDevice(pin = 11)
        self.fsyncPin = gpiozero.OutputDevice(pin = 8)
        self.fsyncPin.on()
        self.clkPin.on()
        self.dataPin.off()
    

    def send16(self, n, cs):
        decoder.enable(cs)
        self.fsyncPin.off()
        mask = 1 << 15
        for i in range(0, 16):
            self.dataPin.value = bool(n & mask)
            self.clkPin.off()
            self.clkPin.on()
            mask = mask >> 1
        self.dataPin.off()
        self.fsyncPin.on()


spi = Spi()

