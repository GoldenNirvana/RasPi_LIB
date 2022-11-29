from Components.WaveGen import WaveGen, WAVE_LIST
from PyQt5 import QtWidgets, uic

SG = WaveGen(0)
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


def main():
    print("Start program...")
    UI.CMB.addItems(WAVE_LIST)
    UI.SLD.valueChanged.connect(updateSLD)
    UI.BTNF.clicked.connect(sendCurrentFreq)
    UI.BTNS.clicked.connect(state)
    UI.CMB.currentIndexChanged.connect(comboBoxChange)
    UI.show()
    APP.exec()


if __name__ == '__main__':
    main()
