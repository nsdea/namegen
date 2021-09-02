import os
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = random.choice(['a', 'b'])
    return render_template('home.html', name=name)

app.run()