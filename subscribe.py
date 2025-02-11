import paho.mqtt.client as mqtt			# Tuodaan kirjastot​
from stepperi import fullRev
import multiprocessing
import scheduler
import time #temp

def on_connect(client, userdata, flags, rc):		# Yhteyden muodostuessa suoritetaan tämä funktio​

    print(f"Connected {rc}")			#   Tulostetaan Connect ja palautuskoodi​
    client.subscribe("tite24")		#   Tilataan clientille rasp/topic aihe​





def on_message(client, userdata, msg):		# Viestin saapuessa suoritetaan tämä funktio​
    message=msg.payload.decode()
    print(message)
    msgtype=message[:3]
    if msgtype == "cfg":
        #etä konfigurointi
        #scheduler.setTimes()
        pass
    elif msgtype == "spn":
        fullRev()

def counter(): #multiprocessing testausta
    counter=1
    while True:
        counter+=1
        print(counter)
        time.sleep(1)


def mqttc():
    client = mqtt.Client()				# Luodaan client
    
    client.on_connect = on_connect			# Clientin on_connect metodiksi liitetään yo. on_connec​

    client.on_message = on_message			# Clientin on_message metodiksi liitetään yo. On_message

    client.will_set('tite24', b'{"status": "Off"}')	# Kerrotaan brokerille LWT aihe (topic) ja viesti

    client.connect("test.mosquitto.org", 1883, 60)	# Yhdistetään client MQTT serveriin (brokeriin)​

    client.loop_forever()				# Toistetaan

p2 = multiprocessing.Process(target=counter) #multiprocessing testausta
p1 = multiprocessing.Process(target=mqttc)


if __name__=="__main__":
    p2.start()
    p1.start()

