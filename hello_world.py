
import paho.mqtt.client as mqtt			# Tuodaan kirjastot​

def on_connect(client, userdata, flags, rc):		# Yhteyden muodostuessa​

    if rc == 0:					# suoritetaan tämä funktio​
        print("Connect OK")​

    else:
        print(f"Connect fail. Error: {rc}")​

client = mqtt.Client() 				# Tehdään client​

client.on_connect = on_connect 			# Liiteään on_connect clientin funktioon​

client.connect("mosquitton.ip.tähän.näin", 1883, 60) 	# Muodostetaan yhteys​

client.loop_forever()