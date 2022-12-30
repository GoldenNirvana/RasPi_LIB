from Components.WaveGen import WaveGen, WAVE_LIST
from Components.AD7705 import AD7705, CHN_AIN1
import threading
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

sg = WaveGen(0) 
sg.stateOn(1000)
sg.setWave(0)
adc = AD7705()
adc.initChannel(CHN_AIN1)

BEGIN = 6000
END = 8000
STEP = 20 
REP = 10


def getResults():
    return adc.readADResultRaw(CHN_AIN1)
    

def main():
    current_datetime = datetime.now()
    print("Current date & time : ", current_datetime)
    str_current_datetime = str(current_datetime)
    str_current_datetime = str_current_datetime[:-7]
    str_current_datetime = str_current_datetime.replace(':', '-')
    #print(str_current_datetime)
    file_name = str_current_datetime + '.txt'
    afc_name = str_current_datetime + '.png'
    #print(file_name)

    for n in range (BEGIN, END, STEP):
        values = []
        for m in range(0,REP):
            sg.send_f(n)
            values.insert(m, getResults())
        values.sort()
        datafile = open("Logs/"+ file_name, 'a+')
        datafile.write(str(n) +' ' + str(values[int(REP / 2) + 2]) + "\n")
        datafile.close()
        
    datafile = open("Logs/"+ file_name, 'a+')
    datafile.write("REP" + str(REP) + "\n" + "STEP" + str(STEP)  + "\n")
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
    print("finish")
    plt.draw()


if __name__ == '__main__':
    main()

