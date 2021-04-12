import sys

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import mysql.connector as mysql
from flask_sqlalchemy import SQLAlchemy
from app.models.models import User



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://banana:banana@mysql:3306/rms'
db = SQLAlchemy(app)


def getMysqlConnection():
    return mysql.connect(user='banana', host='mysql',password="banana", port='3306', database='rms')

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)

#     def __init__(self, id, username):
#         self.id = id
#         self.username = username

#     def __repr__(self):
#         return '<User %r>' % self.username


@app.route('/')
def home():
    return render_template("index.html")
    # return "abc"

@app.route('/db')
def dbroute():
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
@app.route('/api/users', methods=['GET'])
def users():
    rs = User.query.all()
    return jsonify(users=[i.serialize for i in rs]);

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    rs = User.query.get(id)
    return jsonify(user=rs.serialize);

@app.route('/api/users', methods=['POST'])
def set_user():
    # db.create_all() # In case user table doesn't exists already. Else remove it.    
    data = request.json
    print('Request==============')
    print(data)
    user = User(data['id'], data['username'])
    db.session.add(user)
    db.session.commit() # This is needed to write the changes to database
    return  jsonify(user=user.serialize)




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=81)