from Components.WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
from Components.Adc import Adc, CHN_AIN1

import threading
import time


SG = WaveGen(0)  # portOnDecoder, freq(may be Null)

APP = QtWidgets.QApplication([])
UI = uic.loadUi("Interface/window_2.ui")

def updateSLD():
    UI.LCD.display(UI.SLD.value())
    sendCurrentFreq()

        
def sendCurrentFreq():
    if SG.getState():
        SG.setWave(UI.CMB.currentIndex())
        SG.send(UI.SLD.value())


def state():
    if SG.getState():
        SG.stateOff()
        UI.BTNS.setText("RUN")
    else:
        SG.stateOn(UI.SLD.value())
        UI.BTNS.setText("STOP")


def comboBoxChange():
    sendCurrentFreq()


def printResults(x):
    while True:
        print(x.readADResultRaw(CHN_AIN1))
        time.sleep(0.5)


def main():
    #adc = Adc(1, 0)     # bus, ss
    #adc.initChannel(CHN_AIN1)
    print("Start program...")
    testCase = 1
    if testCase == 1:
        UI.CMB.addItems(WAVE_LIST)
        UI.SLD.valueChanged.connect(updateSLD)
        UI.BTNF.clicked.connect(sendCurrentFreq)
        UI.BTNS.clicked.connect(state)
        UI.CMB.currentIndexChanged.connect(comboBoxChange)
        UI.show()
        #threading.Thread(target=printResults, args=[adc]).start()
        APP.exec()
    elif testCase == 2:
        #threading.Thread(target=printResults, args=[adc]).start()
        time.sleep(3)
        SG.stateOn()
        time.sleep(3)
        SG.stateOff()
    elif testCase == 3:
        c = 10000
        SG.stateOn(c)
        SG.setWave(0)
        #SG2.stateOn(c)
        while c < 100000:
            time.sleep(0.2)
            SG.send(c)
            #SG2.send(c)
            c += 1000
            if c > 90000:
                c -= 80000


if __name__ == '__main__':
    main()
