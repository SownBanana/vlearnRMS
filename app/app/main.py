import sys

from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin
import mysql.connector as mysql



app = Flask(__name__)

def getMysqlConnection():
    return mysql.connect(user='banana', host='mysql',password="banana", port='3306', database='rms')


@app.route('/')
def home():
    return render_template("index.html")
    # return "abc"

@app.route('/db')
def db():
    print('==============>');
    db = getMysqlConnection()
    if db :
        return "ok"
    return "not ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=81)