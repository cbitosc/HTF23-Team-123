import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':


        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()


        return render_template('index.html')
    