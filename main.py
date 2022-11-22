from ABC import AD770X, CHN_AIN1
from WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
import spidev
import time
import threading

APP = QtWidgets.QApplication([])
UI = uic.loadUi("window_2.ui")
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000
SG = WaveGen(1, 1000, spi)

abc = AD770X(spidev.SpiDev(),0, 1)
abc.initChannel(CHN_AIN1)

def updateSLD():
    UI.LCD.display(UI.SLD.value())
    if SG.getState():
        sendCurrentFreq()



def sendCurrentFreq():
    SG.setWave(UI.CMB.currentIndex())
    freq = UI.SLD.value()
    SG.setFreq(freq)
    SG.send()
    print("There")


def state():
    if SG.getState():
        SG.stateOff()
        UI.BTNS.setText("RUN")
    else:
        SG.setFreq(UI.SLD.value())
        SG.setFreq(50000)
        SG.stateOn()
        UI.BTNS.setText("STOP")


def comboBoxChange():
    sendCurrentFreq()


def getResults():
    while True:
        print(abc.readADResultRaw(CHN_AIN1))
        time.sleep(0.5)



def main():
    UI.CMB.addItems(WAVE_LIST)
    UI.SLD.valueChanged.connect(updateSLD)
    UI.BTNF.clicked.connect(sendCurrentFreq)
    UI.BTNS.clicked.connect(state)
    UI.CMB.currentIndexChanged.connect(comboBoxChange)
    UI.show()
    threading.Thread(target=getResults).start()
    
    APP.exec()
    

    #SG.stateOn()
    #SG.setFreq()
    #SG.send()


if __name__ == '__main__':
    main()
