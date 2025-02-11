import datetime
import time
import re


badinput="Enter time in (HH:MM) format!"
currTime=str(datetime.datetime.now())[11:19]

print(currTime)


def setTimes(h1=None,h2=None):
    a=re.search('^(?:[01]\d|2[0-3]):[0-5]\d$', h1) #Regex, tarkistaa että syöte on väliltä 00:00-23:59
    b=re.search('^(?:[01]\d|2[0-3]):[0-5]\d$', h2)
    if a != None and b != None:
        pass
        #config
    else:
        return badinput
    
if __name__=="__main__":
    print(setTimes("10:30", "22:30"))