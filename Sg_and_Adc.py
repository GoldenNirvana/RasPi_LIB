from Components.WaveGen import WaveGen, WAVE_LIST
from Components.Adc import Adc, CHN_AIN1
import threading
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

sg = WaveGen(0)   # 0 - decoder port
sg.stateOn(1000)  # 1000 hz
sg.setWave(0)     # 0 = sin
adc = Adc()
adc.initChannel(CHN_AIN1)


def getResults():
    return adc.readADResultRaw(CHN_AIN1)
    

def main():
    
    #threading.Thread(target=printResults, args=[adc]).start()
    #code here...
    
    #.send_f(300)   # send to waveGen
    #x = getResults()
    
    current_datetime = datetime.now()
    print("Current date & time : ", current_datetime)
    str_current_datetime = str(current_datetime)
    str_current_datetime = str_current_datetime[:-7]
    str_current_datetime = str_current_datetime.replace(':', '-')
    print(str_current_datetime)
    # create a file object along with extension
    file_name = str_current_datetime + '.txt'
    afc_name = str_current_datetime + '.png'
    print(file_name)

    for n in range (5000,10000, 30):
        values = []
        for m in range(0,11):
            sg.send_f(n)
            values.insert(m, getResults())
        values.sort()
        #summ += getResults()
        # get current date and time
        #print("File created : ", file.name)
        #file.close()
        #datafile = open("amplitudes.txt", "a+")
        datafile = open("Logs/"+ file_name, 'a+')
        datafile.write(str(n) +' ' + str(values[7]) + "\n")
        datafile.close()

    data2 = np.loadtxt("Logs/"+ file_name)
    x = data2[:, 0]
    y = data2[:, 1]
    plt.plot(x, y, 'r--')
    plt.title('Резонанс датчика')
    plt.xlabel('Частота, КГц')
    plt.ylabel('Амплитуда')
    plt.grid(1)
    plt.savefig("Logs/"+ afc_name, dpi=100)
    plt.show()
    #plt.draw()
    # datafile.write('{} {}'.format(int('0xff', 16), int('0xaa', 16)))


if __name__ == '__main__':
    main()

