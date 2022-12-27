from PyQt5 import QtWidgets, uic

import threading
import time


APP = QtWidgets.QApplication([])
UI = uic.loadUi("../Interface/window_2.ui")

def updateSLD():
    UI.LCD.display(UI.SLD.value())
    sendCurrentFreq()


def funcForImitate(data):
    #code here
    return 10
    
        
def sendCurrentFreq():
    print(UI.SLD.value() ,funcForImitate(UI.SLD.value()))


def main():
    UI.SLD.valueChanged.connect(updateSLD)
    UI.BTNF.clicked.connect(sendCurrentFreq)
    UI.show()
    APP.exec()


if __name__ == '__main__':
    main()

