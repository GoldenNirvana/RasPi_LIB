from Components.WaveGen import WaveGen, WAVE_LIST
from Components.Adc import Adc, CHN_AIN1
import threading
import time

sg = WaveGen(0)   # 0 - decoder port
sg.stateOn(1000)  # 1000 hz
sg.setWave(0)     # 0 = sin
adc = Adc()    
adc.initChannel(CHN_AIN1)

def printResults(x):
    while True:
        print(x.readADResultRaw(CHN_AIN1))
        time.sleep(0.5)


def getResults():
    return adc.readADResultRaw(CHN_AIN1)
    

def main():
    
    #threading.Thread(target=printResults, args=[adc]).start()
    #code here...
    
    sg.send_f(15000)   # send to waveGen
    x = getResults()
    print(x)


if __name__ == '__main__':
    main()

