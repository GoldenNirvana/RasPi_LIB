#from Components.WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
from Components.Adc import Adc, CHN_AIN1

import threading
import time


#SG = WaveGen(0)

APP = QtWidgets.QApplication([])
UI = uic.loadUi("Interface/window_2.ui")

def updateSLD():
    UI.LCD.display(UI.SLD.value())
    sendCurrentFreq()

        
def sendCurrentFreq():
    if SG.getState():
        #print(UI.SLD.value())
        SG.setWave(UI.CMB.currentIndex())
        SG.send_f(UI.SLD.value())


def state():
    if SG.getState():
        SG.stateOff()
        print(UI.SLD.value())
        UI.BTNS.setText("RUN")
        print(1)
    else:
        SG.setWave(UI.CMB.currentIndex())
        SG.stateOn(UI.SLD.value())
        UI.BTNS.setText("STOP")
        print(UI.SLD.value())


def comboBoxChange():
    sendCurrentFreq()


def printResults(x):
    while True:
        print(x.readADResultRaw(CHN_AIN1))
        time.sleep(0.5)


def main():
    adc = Adc()    
    adc.initChannel(CHN_AIN1)
    print("Start program...")
    testCase = 2
    if testCase == 1:
        UI.CMB.addItems(WAVE_LIST)
        UI.SLD.valueChanged.connect(updateSLD)
        UI.BTNF.clicked.connect(sendCurrentFreq)
        UI.BTNS.clicked.connect(state)
        UI.CMB.currentIndexChanged.connect(comboBoxChange)
        UI.show()
        threading.Thread(target=printResults, args=[adc]).start()
        APP.exec()
    elif testCase == 2:
        threading.Thread(target=printResults, args=[adc]).start()
    elif testCase == 3:
        c = 10000
        threading.Thread(target=printResults, args=[adc]).start()
        SG.stateOn(c)
        SG.setWave(0)
        #SG2.stateOn(c)
        while c < 100000:
            time.sleep(0.01)
            SG.send_f(c)
            #SG2.send(c)
            c += 100
            if c > 50000:
                c -= 49000


if __name__ == '__main__':
    main()
