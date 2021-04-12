import sys

from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin
import mysql.connector as mysql
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://banana:banana@mysql:3306/rms'
db = SQLAlchemy(app)


def getMysqlConnection():
    return mysql.connect(user='banana', host='mysql',password="banana", port='3306', database='rms')


@app.route('/')
def home():
    return render_template("index.html")
    # return "abc"

@app.route('/db')
def db():
    print('==============>');
    if db:
        return "ok"
    else :
        return "not ok"
    # try:
    #     db = getMysqlConnection()
    #     return "db ok"
    # except:
    #     return "smth gone not ok"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=81)