from ABC import AD770X, CHN_AIN1
from WaveGen import WaveGen, WAVE_LIST
import spidev
import time
#import threading

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 80000
SG = WaveGen(0, 1000, spi)

#abc = AD770X(spidev.SpiDev(),0, 1)
#abc.initChannel(CHN_AIN1)

#def updateSLD():
    #UI.LCD.display(UI.SLD.value())

#def sendCurrentFreq():
    #SG.setWave(UI.CMB.currentIndex())
SG.stateOn()
SG.setWave(0)
freq = 1000
SG.setFreq(freq)
while SG.stateOn():
    SG.send()
    print("There")
time.sleep(5)
SG.stateOff()
#sendCurrentFreq()

#SG.getState()
#SG.stateOff()
        #UI.BTNS.setText("RUN")
        #SG.setFreq(UI.SLD.value())
#SG.setFreq(50000)
#SG.stateOn()
        #UI.BTNS.setText("STOP")


#def comboBoxChange():
#    sendCurrentFreq()


#def getResults():
#while True:
    #print(abc.readADResultRaw(CHN_AIN1))
    #time.sleep(0.5)

#threading.Thread(target=getResults).start()
#def main():
    #UI.CMB.addItems(WAVE_LIST)
    #UI.SLD.valueChanged.connect(updateSLD)
    #UI.BTNF.clicked.connect(sendCurrentFreq)
    #UI.BTNS.clicked.connect(state)
    #UI.CMB.currentIndexChanged.connect(comboBoxChange)
    #UI.show()

    
#APP.exec()
    

    #SG.stateOn()
    #SG.setFreq()
    #SG.send()


#if __name__ == '__main__':
#main()

