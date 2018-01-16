from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnector import MySQLConnector
import random
app = Flask(__name__)
app.secret_key = 'a'

DB = MySQLConnector(app, 'sorting_hat')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/houses')
def houses():
    query_string = 'SELECT sorting_hat.students.name AS student, sorting_hat.houses.name AS house FROM sorting_hat.students JOIN sorting_hat.houses ON sorting_hat.students.house_id = sorting_hat.houses.id'
    
    results = DB.query_db(query_string)
    print results
    return render_template("houses.html", context=results)

@app.route('/sort', methods=["POST"])
def process():
    print 'submitted name:', request.form['name']
    name = request.form['name']
    house = random.randint(4,4)
    student = {
        'name': name,
        'house': house
    }
    session['student'] = student
    query_string = 'INSERT INTO students (name, house_id) VALUES (:name, :house)'
    print query_string
    DB.query_db(query_string, student)
    return redirect('/houses')








app.run(debug=True)