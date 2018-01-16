from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'logandreg')
app.secret_key = 'aasdfasd'


@app.route('/')
def index():
    print 'server connecting to DB properly'
    return render_template('index.html')

@app.route('/register')
def emails():
    return render_template('register.html')

@app.route('/registered')
def success():
    return render_template('registered.html', users=session['users'])

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    info = mysql.query_db("SELECT * FROM users")
    email_check = False
    password_check = False

    for user in info:
        if user['email'] == email:
            email_check = True
            if user['password'] == password:
                password_check = True
                return render_template('registered.html', users=info)

    if not email_check:
        flash('email is not in our registry')
    elif email_check and not password_check:
        flash('incorrect password')

    return redirect('/')

        

@app.route('/newuser', methods=['POST'])
def newuser():
    username = request.form['username']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    password2 = md5.new(request.form['password2']).hexdigest()
    errors = False

    print 'username:', username
    print 'email:', email
    print 'passsword:', password
    print 'passsword2:', password2

    if not EMAIL_REGEX.match(email):
        flash("that's not how emails are written.")
        errors = True
    if password != password2:
        flash("passwords don't match")
        errors = True
    if len(password) < 8 :
        flash("password must be at least 8 chars long")
        errors = True
    if errors:
        return redirect('/register')

    session['data'] = {
        'username': username,
        'email': email,
        'password': password
    }

    query = "INSERT INTO logandreg.users (username, password, email, date_created, date_updated) VALUES (:username, :password, :email, NOW(), NOW());"
    mysql.query_db(query, session['data'])
    session['users'] = mysql.query_db("SELECT * FROM users")
    flash('try logging in now')
    return render_template('index.html')















app.run(debug=True)

