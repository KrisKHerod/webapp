from flask import Flask, flash, redirect, render_template
import psycopg2
import config


app = Flask(__name__)




# put this into another file
def getData():

	conn_string = "host='%s' port='%s' dbname='%s' user='%s' password='%s'"%(config['db_host'], config['db_port'], config['db_name'], config['db_user_name'], config['db_password'])
	conn = psycopg2.connect(conn_string)

	cursor = conn.cursor()

	if cursor:
		print ("connected to postgresql")

	sql_statement = "SELECT * FROM station_status;"

	cursor.execute(sql_statement)

	station_data = {}


	for station in cursor.fetchall():
		station_data[station[0]] = {
			'group_id': station[1],
			'concentration': station[2],
			'latitude': station[3],
			'longitude': station[4],
			'warning_status': station[5],
			'alert_status': station[6],
			'device_status': station[7]
		}

	return station_data



# put routes into another file
@app.route("/")
def index():
	station_data = getData()
	
	return render_template(
		'index.html', station_data = station_data)



if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000)


