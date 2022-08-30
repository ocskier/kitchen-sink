import time
import flask
from flask import Flask, request, jsonify, render_template

app = flask.Flask(__name__, static_url_path='', static_folder='build', template_folder="build")

app.config["DEBUG"] = True

app.config.from_pyfile('settings.py')

@app.route("/current-time")
def get_timestamp():
    return {'time': time.time()}

@app.route("/")
def my_index():
    return render_template("index.html")
