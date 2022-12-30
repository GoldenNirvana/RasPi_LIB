from spidev import SpiDev

class ad7606():
    #try:
        #start_acq_fd = open("/sys/class/gpio/gpio145/value", 'w', 0)
   # except IOError as e:
       # print("Error opening start acquire gpio pin: %s" % e)
      #  raise

    def __init__(self, dev):
        self.dev = SpiDev()
        try:
            self.dev.open(3,dev)
            self.dev.mode = 2
        except IOError as e:
            print("Error opening /dev/spidev3.%d: %s" % (dev, e))
            raise

    def trigger_acquire(self):
        self.start_acq_fd.write(b'1')
        self.start_acq_fd.write(b'0')

    def read(self):
        self.trigger_acquire()
        buf = self.dev.readbytes(16)
        samples = [0,0,0,0,0,0,0,0]
        for i in xrange(8):
            samples[i] = buf[2*i] << 8 | buf[2*i+1] << 0
        return samples


class beagle_daq():
    def __init__(self):
        self.adc0 = ad7606(0)

    def read(self, channel):
        return self.adc0.read()[channel]

b = beagle_daq()
b.read(1)