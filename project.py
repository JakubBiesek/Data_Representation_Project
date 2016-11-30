# -*- coding: utf-8 -*-
from flask import Flask
from flask_mysqldb import MySQL
#: connection to database
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)
#: database queries which are called on index file by jQuery feature
@app.route('/db')
def index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT data FROM cars WHERE id = 1")
	rv = cur.fetchall()
	return str(rv)

@app.route("/db2")
def db2():
	cur = mysql.connection.cursor()
	cur.execute("SELECT data FROM cars WHERE id = 2")
	rv2 = cur.fetchall()
	return str(rv2)
	
@app.route("/db3")
def db3():
	cur = mysql.connection.cursor()
	cur.execute("SELECT data FROM cars WHERE id = 3")
	rv3 = cur.fetchall()
	return str(rv3)
	#: end of databse queries
@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/veyron") 
def name():         
	return "The Super Sport version of the Veyron is recognised by Guinness World Records as the fastest street-legal production car in the world, with a top speed of 430.9 km/h (267.7 mph), and the roadster Veyron Grand Sport Vitesse version is the fastest roadster in the world, reaching an averaged top speed of 408.84 km/h (254.04 mph) in a test on 6 April 2013."
@app.route("/koenigsegg") 
def koenigsegg(): 
 return "News has been spreading like wildfire around the web that the Koenigsegg ownership fraternity may be about to get a major sporting celebrity among its ranks world champion boxer Floyd Mayweather. Reports say that Mayweather is about to add a Koenigsegg CCXR Trevita to his considerable collection of supercars and that he is paying as much as $4.8million for the privilege."
	
@app.route("/tucsons") 
def tucsons(): 
 return " The figures show 5,069 Tucsons were registered in the first five months of the year. They were followed by Volkswagen Golf registrations of 3,623 with the Ford Focus on 3,289. Others in the Top 10 were the Skoda Octavia, Nissan Qashqai, Toyota Corolla, Ford Fiesta, Toyota Yaris, Volkswagen Passat saloon and Toyota Auris."
#: end of text which will be returnet in html file using jQuery

if __name__ == "__main__":     
	app.run()