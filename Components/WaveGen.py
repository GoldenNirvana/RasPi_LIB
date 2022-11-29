from Components.Decoder import Decoder, SPI_BUS

import gpiozero


WAVE_LIST = ['SIN', 'SQU', 'TRI']
waveforms = [0x2000, 0x2028, 0x2002]


class WaveGen(object):
    def __init__(self, port, freq=None):
        self.__decoder = SPI_BUS
        self.__waveForm = 0x2000 # FIXME
        if freq is not None:
            self.__freq = freq
        else:
            self.__freq = 1000
        self.__isWorked = False
        self.__port = port
        self.__prevFrom = waveforms[0]
        self.dataPin = gpiozero.OutputDevice(pin = 10)
        self.clkPin = gpiozero.OutputDevice(pin = 11)
        self.fsyncPin = gpiozero.OutputDevice(pin = 8)
        self.fsyncPin.on()
        self.clkPin.on()
        self.dataPin.off()
        self.clk_freq = 25.0e6

    @staticmethod
    def __getBytes(integer):
        return divmod(integer, 0x100)

    def setFreq(self, freq):
        self.__freq = freq

    def stateOn(self, freq):
        if self.__decoder is not None:
            self.__decoder.enable(self.__port)
        self.__waveForm = self.__prevFrom
        self.__isWorked = True
        self.send_f(freq)

    def setWave(self, formIndex):
        self.__waveForm = waveforms[formIndex]

    def stateOff(self):
        self.__prevFrom = self.__waveForm
        self.__waveForm = 0x2040
        self.__isWorked = False
        self.send16(0x2040)

    def getForm(self):
        return WAVE_LIST[waveforms.index(self.__waveForm)]

    def getState(self):
        return self.__isWorked
        
    def send_f(self, f):
        if f is not None:
            self.__freq = f
        flag_b28  = 1 << 13
        flag_freq = 1 << 14
        scale = 1 << 28
        n_reg = int(self.__freq * scale / self.clk_freq)
        n_low = n_reg         & 0x3fff
        n_hi  = (n_reg >> 14) & 0x3fff
        
        print(bin(self.__waveForm))
        self.send16(flag_freq | n_low)
        self.send16(flag_freq | n_hi)
        self.send16(self.__waveForm)

    def send16(self, n):
        self.fsyncPin.off()
        mask = 1 << 15
        for i in range(0, 16):
            self.dataPin.value = bool(n & mask)
            print(bool(n & mask))
            self.clkPin.off()
            self.clkPin.on()
            mask = mask >> 1
        self.dataPin.off()
        self.fsyncPin.on()
