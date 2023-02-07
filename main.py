from Components.WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
# from Components.Pot import Pot
 #from Components.AD7705 import AD7705, CHN_AIN1
from Components.AD7606 import Ad7606

import threading
import time

SG = WaveGen(0)
# pot = Pot(1)

APP = QtWidgets.QApplication([])
UI = uic.loadUi("Interface/window_2.ui")


def updateSLD():
    UI.LCD.display(UI.SLD.value())
    sendCurrentFreq()


def updateSLDforPot():
    x = int(UI.SLD.value() * 255 / 15000)
    UI.LCD.display(x)
    pot.setGain(x)


def sendCurrentFreq():
    if SG.getState():
        # print(UI.SLD.value())
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
    # adc = AD7705()
    # adc.initChannel(CHN_AIN1)
    # 1 - SG and ADC
    # 2 - Only ADC
    # 3 - SplineSG and ADC
    # 4 - Only Pot
    # 5 - AD7606
    testCase = 5
    if testCase == 1:
        print("Start case 1")
        UI.CMB.addItems(WAVE_LIST)
        UI.SLD.valueChanged.connect(updateSLD)
        UI.BTNF.clicked.connect(sendCurrentFreq)
        UI.BTNS.clicked.connect(state)
        UI.CMB.currentIndexChanged.connect(comboBoxChange)
        UI.show()
        # threading.Thread(target=printResults, args=[adc]).start()
        APP.exec()
    elif testCase == 2:
        print("Start case 2")
        threading.Thread(target=printResults, args=[adc]).start()
    elif testCase == 3:
        print("Start case 3")
        c = 10000
        # threading.Thread(target=printResults, args=[adc]).start()
        SG.stateOn(c)
        SG.setWave(0)
        while c < 100000:
            time.sleep(0.01)
            SG.send_f(c)
            c += 100
            if c > 50000:
                c -= 49000
    elif testCase == 4:
        print("Start case 4")
        UI.SLD.valueChanged.connect(updateSLDforPot)
        UI.show()
        APP.exec()
    elif testCase == 5:
        ad7606 = Ad7606(0)
        while True:
            print(ad7606.readByAppSpi())
            time.sleep(0.1)


if __name__ == '__main__':
    main()
