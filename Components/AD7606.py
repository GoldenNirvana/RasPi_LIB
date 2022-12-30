import RPi.GPIO as IO
import time

cs = 32
clk = 38
miso = 22
cva = 40
cvb = 18
busy = 36
 
#self.cs = gpiozero.OutputDevice(pin = 12)   # 12 gpio
#self.clk = gpiozero.OutputDevice(pin = 20)  # 20
#self.miso = gpiozero.OutputDevice(pin = 25) # 25
#self.cva = gpiozero.OutputDevice(pin = 21)  # 21
#self.cvb = gpiozero.OutputDevice(pin = 6)  # 
#self.busy = gpiozero.OutputDevice(pin = 16) # 16

IO.setmode(IO.BOARD)
IO.setup(cs, IO.OUT) #
IO.setup(clk, IO.OUT) # 
IO.setup(miso, IO.IN)# 
IO.setup(cva, IO.OUT) #
IO.setup(cvb, IO.OUT) # 
IO.setup(busy, IO.IN) #

def get():
    values = []
    IO.output(cva, 0)
    IO.output(cva, 1)
    IO.output(cvb, 0)
    IO.output(cvb, 1)
    
    while IO.input(busy) == 0:
        print(0)
        pass
    while IO.input(busy) == 1:
        print(1)
        pass
    IO.output(cs, 0)
    
    for i in range(0, 4):
        mask = 1 << 15
        word = ''
        for j in range(0, 16):
            IO.output(clk, 0)
            IO.output(clk, 1)
            bit = IO.input(miso)
            word = word + str(bit)
            mask = mask >> 1
        values.append(word)
        
    IO.output(cs, 1)
    return values


IO.output(cs, 1)
IO.output(cva, 1)
IO.output(cvb, 1)
data = get()
print(data)    
            


            
    