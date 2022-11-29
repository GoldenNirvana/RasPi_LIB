WAVE_LIST = ['SIN', 'SQU', 'TRI']
waveforms = [0x2000, 0x2020, 0x2002]

import spidev


class WaveGen(object):
    def __init__(self, freq, bus, port, decoder=None):
        self.__decoder = decoder
        self.__waveForm = 0x2040 # FIXME
        self.__freq = freq
        self.__clockFreq = 25000000
        self.__isWorked = False
        self.__spi = spidev.SpiDev()
        self.__bus = bus
        self.__port = port
        self.__prevFrom = waveforms[0]
        self.__send(0x0100)  # 0x2100

    def setDecoder(self, decoder):
        self.__decoder = decoder

    @staticmethod
    def __getBytes(integer):
        return divmod(integer, 0x100)

    def __send(self, data):
        self.__spi.open(self.__bus, 0)
        self.__spi.max_speed_hz = 100000
        high, low = self.__getBytes(data)
        self.__spi.xfer([high, low])
        self.__spi.close()

    def setFreq(self, freq):
        self.__freq = freq

    @staticmethod
    def __getFreq(self):
        return self.__freq

    def stateOn(self, freq):
        if self.__decoder is not None:
            self.__decoder.enable(self.__port)
        self.__waveForm = self.__prevFrom
        self.__freq = freq
        self.__isWorked = True
        self.send()

    def setWave(self, formIndex):
        self.__waveForm = waveforms[formIndex]

    def stateOff(self):
        self.__prevFrom = self.__waveForm
        self.__waveForm = 0x2040
        self.__isWorked = False
        self.__send(0x2040)
        if self.__decoder is not None:
            self.__decoder.disable()

    def getForm(self):
        return WAVE_LIST[waveforms.index(self.__waveForm)]

    def getState(self):
        return self.__isWorked

    def send(self, freq=None):
        if freq is not None:
            self.__freq = freq
        word = hex(int(round((self.__freq * 2 ** 28) / self.__clockFreq)))
        MSB = (int(word, 16) & 0xFFFC000) >> 14
        LSB = int(word, 16) & 0x3FFF
        MSB |= 0x4000
        LSB |= 0x4000
        self.__send(LSB)
        self.__send(MSB)
        self.__send(self.__waveForm)
