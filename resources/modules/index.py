from flask import render_template
from app import app

@app.route('/')
def index():
	print 'passbitch'
	return render_template('index.html')
