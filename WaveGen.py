WAVE_LIST = ['SIN', 'SQU', 'TRI']
waveforms = [0x2000, 0x2020, 0x2002]


class WaveGen(object):
    def __init__(self, channel, freq, ss=0):
        self.__channel = channel
        self.__waveForm = waveforms[0]
        self.__freq = freq
        self.__clockFreq = 25000000
        self.__isWorked = True
        self.__ss = ss

    @staticmethod
    def __getBytes(integer):
        return divmod(integer, 0x100)

    def __send(self, data):
        high, low = self.__getBytes(data)
        print(bin(high))
        print(bin(low))
        # self.ss.low()
        # self.spi.send(high)
        # self.spi.send(low)
        # self.ss.high()

    def setFreq(self, freq):
        self.__freq = freq

    def setWave(self, formIndex):
        self.__isWorked = True  # FIXME
        self.__waveForm = waveforms[formIndex]

    def stateOff(self):
        self.__isWorked = False
        self.__waveForm = 0x2040  # FIXME

    def getForm(self):
        return WAVE_LIST[waveforms.index(self.__waveForm)]

    def getState(self):
        return self.__isWorked

    def send(self):
        # Calculate frequency word to send
        word = hex(int(round((self.__freq * 2 ** 28) / self.__clockFreq)))
        # Split frequency word onto its seperate bytes
        MSB = (int(word, 16) & 0xFFFC000) >> 14
        LSB = int(word, 16) & 0x3FFF
        # Set control bits DB15 = 0 and DB14 = 1; for frequency register 0
        MSB |= 0x4000
        LSB |= 0x4000
        self.__send(0x2100)
        # Set the frequency
        self.__send(LSB)  # lower 14 bits
        self.__send(MSB)  # Upper 14 bits
        self.__send(self.__waveForm)
