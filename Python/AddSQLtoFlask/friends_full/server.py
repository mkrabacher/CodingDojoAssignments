from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print 'server connecting to DB properly'
    return render_template('index.html', friends=friends)

@app.route('/new', methods=['POST'])
def search():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }
    query = "INSERT INTO friends.friends (first_name, last_name, age, friend_since) VALUES (:first_name, :last_name, :age, NOW());"
    friends = mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
















app.run(debug=True)

