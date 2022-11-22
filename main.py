from Components.WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
from Components.ABC import Abc, CHN_AIN1
import threading
import time

# Узел - минус

SG = WaveGen(10000, 0, 0)  # freq, bus, ss  # FIXME 
APP = QtWidgets.QApplication([])
UI = uic.loadUi("Interface/window_2.ui")

def updateSLD():
    UI.LCD.display(UI.SLD.value())
    sendCurrentFreq()
        
        
        
def sendCurrentFreq():
    if SG.getState():
        SG.setWave(UI.CMB.currentIndex())
        SG.send(UI.SLD.value())
        print(UI.SLD.value())


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
    #abc = Abc(0, 1)     # bus, ss
    #abc.initChannel(CHN_AIN1)
    print("helol")
    testCase = 3
    if testCase == 1:
        UI.CMB.addItems(WAVE_LIST)
        UI.SLD.valueChanged.connect(updateSLD)
        UI.BTNF.clicked.connect(sendCurrentFreq)
        UI.BTNS.clicked.connect(state)
        UI.CMB.currentIndexChanged.connect(comboBoxChange)
        UI.show()
        #threading.Thread(target=printResults, args=[abc]).start()
        APP.exec()
    elif testCase == 2:
        threading.Thread(target=printResults, args=[abc]).start()
        time.sleep(3)
        SG.stateOn()
        time.sleep(3)
        SG.stateOff()
    elif testCase == 3:
        c = 10000
        SG.stateOn(c)
        while c < 100000:
            time.sleep(0.05)
            SG.send(c)
            c += 1000
            if c > 90000:
                c -= 80000
    
    
if __name__ == '__main__':
    main()
