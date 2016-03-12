from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
	app.run()

@app.route('/')
def show_interface():
	# Load data from sensors and pass to webpage
	
	return render_template('index.html')

