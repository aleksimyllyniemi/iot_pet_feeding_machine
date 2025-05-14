import os

from flask import Flask, redirect, render_template, request
from flask_socketio import SocketIO
import sqlite3
import eventlet

app = Flask(__name__, static_url_path='', static_folder='static')

socketio = SocketIO(app, async_mode='eventlet')

#tietokannan teko
yhteys = sqlite3.connect("mittaukset.db3")
kursori = yhteys.cursor()
kursori.execute("CREATE TABLE IF NOT EXISTS mittaukset (id INTEGER PRIMARY KEY, aika TEXT, mittaus INTEGER)")
yhteys.commit()
yhteys.close()

mittaukset = dict()

@app.route('/', methods=['GET'])
def index():
   mittaustiedot = dict()

   yhteys = sqlite3.connect("mittaukset.db3")
   kursori = yhteys.cursor()
   kursori.execute("SELECT aika, mittaus FROM mittaukset")

   tiedot = kursori.fetchall()
   for aika in tiedot:
      mittaustiedot[aika[0]] = aika[1]

   yhteys.commit()
   yhteys.close()

   print('Request for index page received')
   return render_template('chart.html', taulukko = mittaustiedot)

@app.route('/lisaa_tieto', methods=['POST'])
def lisaa_tieto():
   data = request.get_json(force=True)
   mittaustulos_lista = data['mittaus']

   yhteys = sqlite3.connect("mittaukset.db3")
   kursori = yhteys.cursor()
   kursori.execute("INSERT INTO mittaukset (aika, mittaus) VALUES (?,?)", (mittaustulos_lista[0], mittaustulos_lista[1]))
   yhteys.commit()
   yhteys.close()

   print("mittaustulos:", mittaustulos_lista)
   socketio.emit('data_update')
   return "200"

if __name__ == '__main__':
   #app.run()
   socketio.run(app, debug=True)
