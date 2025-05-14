import paho.mqtt.client as mqtt			# Tuodaan kirjastot​
from stepperi import fullRev
import time
import datetime
import random
import requests
import json
from grove.display.jhd1802 import JHD1802

#from gpiozero import Buzzer

lcd = JHD1802()
#buzzer = Buzzer(16)

def on_connect(client, userdata, flags, rc):		# Yhteyden muodostuessa suoritetaan tämä funktio​
    print(f"Connected {rc}")			#   Tulostetaan Connect ja palautuskoodi​
    client.subscribe("tite24")		#   Tilataan clientille rasp/topic aihe​

def setTime():
    lastFed=str(datetime.datetime.now())[11:16]
    print(lastFed)
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.write(f"Viim. ruokittu")
    lcd.setCursor(1,0)
    lcd.write(f"Klo {lastFed}")
    """buzzer.on()
    time.sleep(1)
    buzzer.off()"""

def sendmsg(outp):
	client.publish("tite24", payload=outp, qos=0, retain=False)

def on_message(client, userdata, msg):		# Viestin saapuessa suoritetaan tämä funktio​
    message=msg.payload.decode()
    print(message)
    msgtype=message[:3]
    now = str(datetime.datetime.now())[:19]
    #timea = str(datetime.datetime.now())
    amt = random.randint(100,130) #mock data
    if msgtype == "spn":
        fullRev()
        setTime()
        sendmsg(f"Ruokittu {now} {amt}g")
        lähetys = {"mittaus" : (now, amt)}
        viesti = json.dumps(lähetys)
        requests.post("https://tite24-mittaukset-ek-ahdefafzdtcsaqhh.northeurope-01.azurewebsites.net/lisaa_tieto", data=viesti)
    elif msgtype == "spd":
        for i in range(3):
            fullRev()
        sendmsg(f"Ruokittu {now} {amt*3}g")
        lähetys = {"mittaus" : (now, amt*3)}
        viesti = json.dumps(lähetys)
        requests.post("https://tite24-mittaukset-ek-ahdefafzdtcsaqhh.northeurope-01.azurewebsites.net/lisaa_tieto", data=viesti)
    elif message=="Väärä syöte" or message[0:8]=="Ruokittu":
        pass
    else:
	    sendmsg("Väärä syöte")


client = mqtt.Client()				# Luodaan client

client.on_connect = on_connect			# Clientin on_connect metodiksi liitetään yo. on_connec​

client.on_message = on_message			# Clientin on_message metodiksi liitetään yo. On_message

client.will_set('tite24', b'{"status": "Off"}')	# Kerrotaan brokerille LWT aihe (topic) ja viesti

client.connect("broker.emqx.io", 1883, 60)	# Yhdistetään client MQTT serveriin (brokeriin)​

client.loop_forever()				# Toistetaan



if __name__=="__main__":
    pass

