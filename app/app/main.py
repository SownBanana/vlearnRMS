import sys
from os import environ
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import mysql.connector as mysql
app = Flask(__name__)

def getMysqlConnection():
    return mysql.connect(
        host='vlearn.cw9qycdz5bjl.ap-southeast-1.rds.amazonaws.com',
        user='admin', 
        password="Phamson2699", 
        port='3306', 
        database='vlearn')

db = getMysqlConnection()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/db')
def dbroute():
    print('==============>');
    getMysqlConnection()
    return "OK"

@app.route('/api/users', methods=['GET'])
def users():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users")

    results = cursor.fetchall()

    rs = ""
    print(results)
    for result in results:
        rs += ' '.join(map(str,result)) + '\n'
    
    return rs 

@app.route('/api/train', methods=['GET'])
def train():
    cursor = db.cursor()

    cursor.execute("SELECT student_id, course_id, rate FROM course_student")

    results = cursor.fetchall()

    rs = ""
    print(results)
    for result in results:
        rs += ' '.join(map(str,result)) + '\n'
    
    return rs 


@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    rs = User.query.get(id)
    return jsonify(user=rs.serialize);


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=81)