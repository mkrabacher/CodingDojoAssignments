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

@app.route('/friends/<friend_id>', methods=['POST'])
def search(friend_id):
    query = "SELECT * FROM  friends WHERE id = specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
















app.run(debug=True)

