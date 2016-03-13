from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from htu21d import HTU21D
import time

app = Flask(__name__)

@app.route('/')
def index():
	# Load data from sensors and pass to webpage
	sensor = HTU21D()
	sensor.reset()
	time2 = time.asctime()
	temperature = "{:4.2f}".format(sensor.get_temp())
	humidity = "{:4.2f}".format(sensor.get_rel_humidity())
	return render_template('index.html',time=time2,temperature=temperature,humidity=humidity)

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
