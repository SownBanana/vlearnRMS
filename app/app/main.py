import sys
import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd 
import mysql.connector as mysql
from app.models.CF import CF
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/ex.txt')

global rms  

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
    print("Users ===========>")
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
    global rms  
    print("Train ===========>")
    cursor = db.cursor()

    cursor.execute("SELECT student_id, course_id, rate FROM course_student WHERE rate IS NOT NULL")

    results = cursor.fetchall()

    rs = ""
    print(results)
    for result in results:
        rs += ' '.join(map(str,result)) + '\n'

    Y_data = np.asarray(results)

    print("==Y_data")
    print(Y_data)

    # r_cols = ['user_id', 'item_id', 'rating']
    # ratings = pd.read_csv(data_file, sep = ' ', names = r_cols, encoding='latin-1')
    # Y_data_test = ratings.to_numpy()
    
    # print("==Y_data_test")
    # print(Y_data_test)

    rms = CF(Y_data, k = 2)
    rms.fit()

    return jsonify({"status":"success"})


@app.route('/api/users/<int:id>', methods=['GET'])
def recommend_user(id):
    # global rms  
    try:
        recommended_items = rms.recommend(id)
        print ('Recommendation item: ', recommended_items, ' for user ', id)
    except:
        train()
        recommended_items = rms.recommend(id)
        print ('Recommendation item: ', recommended_items, ' for user ', id)
    return jsonify(recommended_items)

@app.route('/api/users/all', methods=['GET'])
def recommend_all():
    # global rms  
    try:
        rs = rms.print_recommendation()
    except:
        train()
        rs = rms.print_recommendation()
    return jsonify(rs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=81)