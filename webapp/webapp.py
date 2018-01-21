from flask import Flask, flash, redirect, render_template
import psycopg2


app = Flask(__name__)



def getData():

	conn_string = "host='test2.cw2k4n8fpsxx.us-west-2.rds.amazonaws.com' port='5432' dbname='test' user='test' password='testcluster'"
	conn = psycopg2.connect(conn_string)

	cursor = conn.cursor()

	if cursor:
		print ("connected to postgresql")

	sql_statement = "SELECT * FROM "




@app.route("/")
def index():
	return "Hdsf"


@app.route("/index/")
def hello(name):
	return render_template(
		'index.html', name=name)



if __name__=="__main__":
	app.run()


