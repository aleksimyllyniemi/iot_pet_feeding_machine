from gpiozero import OutputDevice
import time


a=OutputDevice(22)
b=OutputDevice(24)
c=OutputDevice(23)
d=OutputDevice(25)


def pyori(yks, kaks):
    yks.off()
    kaks.on()
    time.sleep(0.004)


def fullRev(): #360 degree rotation
    for i in range(1,180):
        pyori(d,a)
        pyori(a,b)
        pyori(b,c)
        pyori(c,d)
    pinOff()

def pinOff():
    a.off()
    b.off()
    c.off()
    d.off()


if __name__=="__main__":
    fullRev()