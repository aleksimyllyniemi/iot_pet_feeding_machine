
from gpiozero import OutputDevice
import time


a=OutputDevice(22)
b=OutputDevice(24)
c=OutputDevice(23)
d=OutputDevice(25)

#GND GPIO PIN (0,2), PIN (1,4)

reset=input("a aloittaa, muu asettaa kaikki GPIO pinit low tilaan")

#steps = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def pyori(yks, kaks):
    yks.off()
    kaks.on()
    time.sleep(0.004)

def twoStep(one,two,three,four):
    one.on()
    two.on()
    three.off()
    four.off()
    time.sleep(0.04)

if reset == "a":
    while True:
        pyori(d,a)
        pyori(a,b)
        pyori(b,c)
        pyori(c,d)
elif reset == "b":
    while True:
        twoStep(a,b,c,d)
        twoStep(b,c,d,a)
        twoStep(c,d,a,b)
        twoStep(d,a,b,c)

else:
    a.off()
    b.off()
    c.off()
    d.off()

