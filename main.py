from Components.WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
from Components.ABC import Abc, CHN_AIN1

import threading
import time

APP = QtWidgets.QApplication([])
UI = uic.loadUi("Interface/window_2.ui")


def updateSLD():
    UI.LCD.display(UI.SLD.value())
    if SG.getState():
        sendCurrentFreq()


def sendCurrentFreq():
    SG.setWave(UI.CMB.currentIndex())
    freq = UI.SLD.value()
    SG.setFreq(freq)
    SG.send()


def state():
    if SG.getState():
        SG.stateOff()
        UI.BTNS.setText("RUN")
    else:
        SG.setFreq(UI.SLD.value())
        SG.stateOn()
        UI.BTNS.setText("STOP")


def comboBoxChange():
    sendCurrentFreq()


def foo(x):
    while True:
        print(x.readADResultRaw(CHN_AIN1))
        time.sleep (0.5)

def main():
    abc = Abc(0, 1)     # bus, ss
    SG = WaveGen(0, 0, 0)  # freq, bus, ss  # FIXME 
    abc.initChannel(CHN_AIN1)
    
    a = 2
    if a == 1:
        UI.CMB.addItems(WAVE_LIST)
        UI.SLD.valueChanged.connect(updateSLD)
        UI.BTNF.clicked.connect(sendCurrentFreq)
        UI.BTNS.clicked.connect(state)
        UI.CMB.currentIndexChanged.connect(comboBoxChange)
        UI.show()
        threading.Thread(target=foo).start()
        APP.exec()
    elif a == 2:
        threading.Thread(target=foo, args=[abc]).start()
        time.sleep(3)
        SG.stateOn()
        time.sleep(3)
        SG.stateOff()
        #spi.open(0, 0)
        #SG.stateOff()
    
        
    

    
if __name__ == '__main__':
    main()
