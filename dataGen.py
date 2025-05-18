import requests
import json
import datetime
import random
import time



for i in range(3):
    time.sleep(2)
    now = str(datetime.datetime.now())[:19]
    amt = random.randint(100,130) #mock data
    lähetys = {"mittaus" : (now, amt*3)}
    viesti = json.dumps(lähetys)
    requests.post("http://127.0.0.1:5000/lisaa_tieto", data=viesti)