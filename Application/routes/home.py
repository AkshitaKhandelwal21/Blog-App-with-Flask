from Application import app
from flask import render_template

@app.route('/', methods=['GET'])
def home():
    return 'Home'
