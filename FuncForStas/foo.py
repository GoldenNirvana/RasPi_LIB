import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.optimize import curve_fit
from PyQt5 import QtWidgets, uic
from datetime import datetime

import threading
import time


APP = QtWidgets.QApplication([])
UI = uic.loadUi("../Interface/window_2.ui")

def updateSLD():
    UI.LCD.display(UI.SLD.value())
    sendCurrentFreq()


def funcForImitate(data):
    #code here
    a = 30000/np.sqrt((4000*4000-data*data)**2+4*20*data*data)
    return a

def sendCurrentFreq(n):
    print(n,funcForImitate(n))

def func(x, p1, p2):
    return p1 * np.cos(p2 * x) + p2 * np.sin(p1 * x)

def main():
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

    for n in range (3800,4200):
        sendCurrentFreq(n)
        # get current date and time
        #print("File created : ", file.name)
        #file.close()
        #datafile = open("amplitudes.txt", "a+")
        datafile = open(file_name, 'a+')
        datafile.write(str(n) +' ' + str(funcForImitate(n)) + "\n")
        datafile.close()

    data2 = np.loadtxt(file_name)
    x = data2[:, 0]
    y = data2[:, 1]
    plt.plot(x, y, 'r--')
    plt.title('Резонанс датчика')
    plt.xlabel('Частота, КГц')
    plt.ylabel('Амплитуда')
    plt.grid(1)
    plt.savefig(afc_name, dpi=100)
    plt.show()
    plt.draw()
    # datafile.write('{} {}'.format(int('0xff', 16), int('0xaa', 16)))


if __name__ == '__main__':
    main()

