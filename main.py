from WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic


APP = QtWidgets.QApplication([])
UI = uic.loadUi("window_2.ui")

SG = WaveGen(1, 1000)


def updateSLD():
    UI.LCD.display(UI.SLD.value())


def sendCurrentFreq():
    n = UI.CMB.currentIndex()
    SG.setWave(n)
    freq = UI.SLD.value()
    SG.setFreq(freq)
    SG.send()


def BTNSclik():
    SG.stateOff()
    SG.send()


def main():
    UI.CMB.addItems(WAVE_LIST)
    UI.SLD.valueChanged.connect(updateSLD)
    UI.BTNF.clicked.connect(sendCurrentFreq)
    UI.BTNS.clicked.connect(BTNSclik)
    UI.show()
    APP.exec()
    # print(SG.GetForm())
    # print(SG.GetFreq)
    # print(SG.GetState())


if __name__ == '__main__':
    main()
