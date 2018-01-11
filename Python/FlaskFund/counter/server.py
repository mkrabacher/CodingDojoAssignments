from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

session['counter'] = 0
@app.route('/')
def index():
    session['counter'] += 1
    return render_template("index.html")

app.run(debug=True)
