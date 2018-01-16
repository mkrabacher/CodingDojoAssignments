from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'users')
app.secret_key = 'aasdfasd'

@app.route('/')
def index():    
    return redirect('/users')

@app.route('/users')
def users():    
    users = mysql.query_db("SELECT * FROM users")
    print 'server connecting to DB properly'
    return render_template('index.html', users=users)

@app.route('/users/new')
def new():
    return render_template('newuser.html')

@app.route('/users/create', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    if len(email) < 1:
        flash("Email can't be empty num nuts")
        return redirect('/newUser')
    elif not EMAIL_REGEX.match(email):
        flash("that's not how emails are written.")
        return redirect('/newUser')

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    query = "INSERT INTO users.users (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW());"
    mysql.query_db(query, data)

    userid = mysql.query_db("SELECT * FROM users WHERE first_name='" + data['first_name'] + "' AND last_name='" + data['last_name'] + "'")
    return redirect('/users/'+ str(userid[0]['id']))

@app.route('/users/<id>')
def show(id):
    user = mysql.query_db("SELECT * FROM users WHERE id=" + id)
    return render_template('user.html', user=user)

@app.route('/users/<id>/edit')
def edit(id):
    user = mysql.query_db("SELECT * FROM users WHERE id=" + id)
    return render_template('edit.html', user=user)

@app.route('/update', methods=['POST'])
def update():
    updateUser = {
        'id':request.form['id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    if len(updateUser['email']) < 1:
        flash("Email can't be empty num nuts")
        return redirect('/users/' + updateUser['id'] + '/edit')
    elif not EMAIL_REGEX.match(updateUser['email']):
        flash("that's not how emails are written.")
        return redirect('/users/' + updateUser['id'] + '/edit')
    print 'here'

    query = 'UPDATE users.users SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id'
    mysql.query_db(query, updateUser)
    return redirect('/users/' + updateUser['id'])

@app.route('/users/<id>/destroy')
def destroy(id):
    mysql.query_db("DELETE FROM users WHERE id=" + id)
    return redirect('/users')
















app.run(debug=True)

