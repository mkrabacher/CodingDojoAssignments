from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')
app.secret_key = 'aasdfasd'

alist = [0,1,2,3,4,5,6]

def reverse(arr):
    for i in range(0, len(arr)/2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr

@app.route('/')
def index():
    print 'server connecting to DB properly'
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/the_wall')
def success():
    users = mysql.query_db("SELECT * FROM users")
    posts = reverse(mysql.query_db("SELECT * FROM posts"))
    comments = mysql.query_db("SELECT * FROM comments")
    return render_template('the_wall.html', current_user=session['current_user'], users=users, posts=posts, comments=comments)

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    users = mysql.query_db("SELECT * FROM users")
    email_check = False
    password_check = False

    for user in users:
        if user['email'] == email:
            email_check = True
            if user['password'] == password:
                password_check = True
                session['current_user'] = {
                    'id':user['id'],
                    'first_name':user['first_name'],
                    'last_name':user['last_name'],
                    'email':user['email']
                }
                return redirect('/the_wall')

    if not email_check:
        flash('email is not in our registry')
    elif email_check and not password_check:
        flash('incorrect password')

    return redirect('/')

@app.route('/logoff')
def logoff():
    session.clear()
    return redirect('/')

@app.route('/newuser', methods=['POST'])
def newuser():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    password2 = md5.new(request.form['password2']).hexdigest()
    errors = False

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

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    }

    query = "INSERT INTO the_wall.users (first_name, last_name, password, email, date_created, date_updated) VALUES (:first_name, :last_name, :password, :email, NOW(), NOW());"
    mysql.query_db(query, data)
    flash('try logging in now')
    return render_template('index.html')

@app.route('/newpost', methods=['POST'])
def newpost():
    data = {
        'new_post':request.form['post'],
        'current_user':str(session['current_user']['id'])
    }
    
    query = "INSERT INTO the_wall.posts (post, date_created, date_updated, users_id) VALUES (:new_post, NOW(), NOW(), :current_user);"
    mysql.query_db(query, data)
    return redirect('/the_wall')

@app.route('/comment', methods=['POST'])
def comment():
    data = {
        'new_comment':request.form['comment'],
        'posts_id':request.form['post_id'],
        'current_user':str(session['current_user']['id'])
    }
    
    query = "INSERT INTO the_wall.comments (comment, date_created, date_updated, users_id, posts_id) VALUES (:new_comment, NOW(), NOW(), :current_user, :posts_id);"
    mysql.query_db(query, data)
    return redirect('/the_wall')

@app.route('/del_post', methods=['POST'])
def del_post():
    posts_id = request.form['post_id']

    commentsQuery = "DELETE FROM the_wall.comments WHERE posts_id=" + posts_id
    query = "DELETE FROM the_wall.posts WHERE id=" + posts_id

    mysql.query_db(commentsQuery)
    mysql.query_db(query)
    return redirect('/the_wall')

@app.route('/del_com', methods=['POST'])
def del_com():
    comment_id = request.form['comment_id']

    query = "DELETE FROM the_wall.comments WHERE id=" + comment_id
    
    mysql.query_db(query)
    return redirect('/the_wall')









app.run(debug=True)

