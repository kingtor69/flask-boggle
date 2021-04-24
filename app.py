from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"

from boggle import Boggle

boggle_game = Boggle()

@app.route('/')
def load_home_page():
    return render_template('home.html')

