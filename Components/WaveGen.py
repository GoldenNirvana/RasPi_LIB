#from Config.Spi import Spi, spi
from Config.Spi import decoder
import spidev


WAVE_LIST = ['SIN', 'SQU', 'TRI']
waveforms = [0x2000, 0x2028, 0x2002]


class WaveGen(object):
    def __init__(self, port, freq=None):
        #self.__spi = spi
        self.__spi = spidev.SpiDev(0, 0)
        self.__spi.max_speed_hz = 10000
        self.__spi.bits_per_word = 8
        self.__spi
        self.__waveForm = 0x2000
        if freq is not None:
            self.__freq = freq
        else:
            self.__freq = 1000
        self.__isWorked = False
        self.__port = port
        self.clk_freq = 25.0e6
        #self.__spi.send16(0x2040, port)
        decoder.enable(self.__port)
        self.__spi.xfer([0x2040])

    @staticmethod
    def __getBytes(integer):
        return divmod(integer, 0x100)

    def setFreq(self, freq):
        self.__freq = freq

    def stateOn(self, freq):
        self.__isWorked = True
        self.send_f(freq)

    def setWave(self, formIndex):
        self.__waveForm = waveforms[formIndex]

    def stateOff(self):
        self.__isWorked = False
        #self.__spi.send16(0x2040, self.__port)
        decoder.enable(self.__port)
        self.__spi.xfer([0x2040])

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
        
        decoder.enable(self.__port)
        a, b = self.__getBytes(flag_freq | n_low)
        self.__spi.xfer([a])
        self.__spi.xfer([b])
        a, b = self.__getBytes(flag_freq | n_hi)
        self.__spi.xfer([a, b])
        a, b = self.__getBytes(self.__waveForm)
        self.__spi.xfer([a, b])
        #self.__spi.send16(flag_freq | n_low, self.__port)
        #self.__spi.send16(flag_freq | n_hi, self.__port)
        #self.__spi.send16(self.__waveForm, self.__port)
