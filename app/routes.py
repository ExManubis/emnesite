# IMPORTS
from flask import render_template
from app import app

# FLASK ROUTES
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')