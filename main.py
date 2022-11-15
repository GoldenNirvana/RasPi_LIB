from WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic
import spidev

APP = QtWidgets.QApplication([])
UI = uic.loadUi("window_2.ui")

SG = WaveGen(1, 1000)


def updateSLD():
    UI.LCD.display(UI.SLD.value())
    if SG.getState():
        sendCurrentFreq()


def sendCurrentFreq():
    n = UI.CMB.currentIndex()
    SG.setWave(n)
    freq = UI.SLD.value()
    SG.setFreq(freq)
    SG.send()


def state():
    if SG.getState():
        SG.stateOff()
        UI.BTNS.setText("RUN")
    else:
        SG.stateOn()
        UI.BTNS.setText("STOP")


def main():
    UI.CMB.addItems(WAVE_LIST)
    UI.SLD.valueChanged.connect(updateSLD)
    UI.BTNF.clicked.connect(sendCurrentFreq)
    UI.BTNS.clicked.connect(state)
    UI.show()
    APP.exec()


if __name__ == '__main__':
    main()
