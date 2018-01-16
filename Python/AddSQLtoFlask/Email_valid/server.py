from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = 'aasdfasd'


@app.route('/')
def index():
    print 'server connecting to DB properly'
    return render_template('index.html')

@app.route('/emails')
def emails():
    return render_template('emails.html', emails=session['emails'], submitted_email=session['email'])


#delete don't work and I can't figure out why.
# @app.route('/delete')
# def delete():
#     print 'hello'
#     del_ID = request.form['del_id']
#     print del_ID
#     query = "DELETE FROM emails.emails WHERE id=" + del_ID
#     mysql.query_db(query)
#     return redirect('/emails')

@app.route('/new', methods=['POST'])
def new():
    session['email'] = request.form['email']
    if len(session['email']) < 1:
        flash("Email can't be empty num nuts")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("that's not how emails are written.")
        return redirect('/')

    data = {
        'email': session['email']
    }

    query = "INSERT INTO emails.emails (email, date_created, date_updated) VALUES (:email, NOW(), NOW());"
    mysql.query_db(query, data)
    session['emails'] = mysql.query_db("SELECT * FROM emails")
    return redirect('/emails')















app.run(debug=True)

