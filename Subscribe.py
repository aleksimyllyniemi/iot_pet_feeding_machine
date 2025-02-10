import paho.mqtt.client as mqtt			# Tuodaan kirjastot​
from stepperi import fullRev

def on_connect(client, userdata, flags, rc):		# Yhteyden muodostuessa suoritetaan tämä funktio​

    print(f"Connected {rc}")			#   Tulostetaan Connect ja palautuskoodi​
    client.subscribe("tite24")		#   Tilataan clientille rasp/topic aihe​

def configureFeeder(inpt):
    print("toimii", inpt)  #Koodiajne
    pass





def on_message(client, userdata, msg):		# Viestin saapuessa suoritetaan tämä funktio​

    print(f"{msg.topic} {msg.payload}")		#   Tulostetaan viesti
    message=msg.payload.decode()
    print(message)
    configureFeeder(message)

client = mqtt.Client()				# Luodaan client

client.on_connect = on_connect			# Clientin on_connect metodiksi liitetään yo. on_connec​

client.on_message = on_message			# Clientin on_message metodiksi liitetään yo. On_message

client.will_set('tite24', b'{"status": "Off"}')	# Kerrotaan brokerille LWT aihe (topic) ja viesti

client.connect("test.mosquitto.org", 1883, 60)	# Yhdistetään client MQTT serveriin (brokeriin)​

client.loop_forever()				# Toitetaan