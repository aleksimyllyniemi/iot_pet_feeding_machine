import paho.mqtt.client as mqtt			# Tuodaan kirjastot​
#from stepperi import fullRev
import multiprocessing
import time
import datetime
import re
import os
import signal



def setTimes(h1=None,h2=None):
    badinput="Enter time in (HH:MM) format!"
    print(h1)
    print(h2)
    a=re.search(r'^(?:[01]\d|2[0-3]):[0-5]\d$', h1) #Regex, tarkistaa että syöte on väliltä 00:00-23:59
    b=re.search(r'^(?:[01]\d|2[0-3]):[0-5]\d$', h2)
    if a != None and b != None:
        return [a,b]
    else:
        return badinput


def on_connect(client, userdata, flags, rc):		# Yhteyden muodostuessa suoritetaan tämä funktio​

    print(f"Connected {rc}")			#   Tulostetaan Connect ja palautuskoodi​
    client.subscribe("tite24")		#   Tilataan clientille rasp/topic aihe​


def counter(t1, t2):
    print("reset")
    early=min(t1,t2)
    late=max(t1,t2)
    while True:
        currtime=str(datetime.datetime.now())[11:16]
        if currtime == t1 or currtime == t2:
            #fullRev()
            print("pyörii")
        
        print(currtime)
        time.sleep(60)
        print(type(currtime))

        #nextfeed=???             #Displayed on the lcd
        #lastfeed=currtime     #Displayed on the lcd


def on_message(client, userdata, msg):		# Viestin saapuessa suoritetaan tämä funktio​
    message=msg.payload.decode()
    print(message)
    msgtype=message[:3]
    if msgtype == "cfg":
        times=setTimes(message[4:9],message[10:15])
        print(times)
        print("cfg viesti")
    elif msgtype == "spn":
        #fullRev()
        pass
        

def mqttc():

    client = mqtt.Client()				# Luodaan client
    
    client.on_connect = on_connect			# Clientin on_connect metodiksi liitetään yo. on_connec​

    client.on_message = on_message			# Clientin on_message metodiksi liitetään yo. On_message

    client.will_set('tite24', b'{"status": "Off"}')	# Kerrotaan brokerille LWT aihe (topic) ja viesti

    client.connect("test.mosquitto.org", 1883, 60)	# Yhdistetään client MQTT serveriin (brokeriin)​

    client.loop_forever()				# Toistetaan



if __name__=="__main__":
    t1="15:10"
    t2="22:30"
    found_event=multiprocessing.Event()
    p2 = multiprocessing.Process(target=counter, args=(t1,t2))
    p1 = multiprocessing.Process(target=mqttc, args=())
    
    p2.start()
    p1.start()