from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnector import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'books')

@app.route('/')
def index():
    books = mysql.query_db("SELECT * FROM my_books")
    print 'server connecting to DB properly'
    return render_template('index.html', books=books)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/updatePage/<id>')
def updatePage(id):
    book = mysql.query_db("SELECT * FROM my_books WHERE id=" + id)
    print book
    return render_template('update.html', book=book)

@app.route('/new', methods=['POST'])
def new():
    title = request.form['title']
    author = request.form['author']
    query = "INSERT INTO books.my_books (title, author, date_added) VALUES (:title, :author, NOW());"
    data = {
        'title': title,
        'author': author,
        }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    author = request.form['author']
    id = request.form['id']
    title = request.form['title']
    query = "UPDATE books.my_books SET title='" + title + "', author='" + author + "' WHERE id='" + id + "';"
    mysql.query_db(query)
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    del_id = id
    print del_id
    query = 'DELETE FROM books.my_books WHERE id =' + del_id
    mysql.query_db(query)
    return redirect('/')
















app.run(debug=True)

