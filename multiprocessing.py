import paho.mqtt.client as mqtt			# Tuodaan kirjastot​
import multiprocessing
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected")
    client.subscribe("tite24")

def on_message(client, userdata, msg):		# Viestin saapuessa suoritetaan tämä funktio​

    	print(f"{msg.topic} {msg.payload}")		#   Tulostetaan viesti​

def counter():

    counter=1
    while True:
        counter+=1
        print(counter)
        time.sleep(1)


def mqttRun():

    client = mqtt.Client()				# Luodaan client​

    client.on_connect = on_connect			# Clientin on_connect metodiksi liitetään yo. on_connect​

    client.on_message = on_message			# Clientin on_message metodiksi liitetään yo. On_message​

    client.will_set('rasp/status', b'{"status": "Off"}')	# Kerrotaan brokerille LWT aihe (topic) ja viesti

    client.connect("test.mosquitto.org", 1883, 60)	# Yhdistetään client MQTT serveriin (brokeriin)​

    client.loop_forever()				# Toitetaan

p2 = multiprocessing.Process(target=counter)
p1 = multiprocessing.Process(target=mqttRun)


if __name__=="__main__":
    p2.start()
    p1.start()

