from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

var = 0

@app.route('/')
def index():
    if 'counter' in session:
        if session['inc'] == 1:
            session['counter'] += 1
        elif session['inc'] == 2:
            session['counter'] += 2
    return render_template("index.html")

@app.route('/process')
def process():
    if not 'counter' in session:
        session['counter'] = 0
        session['inc'] = 1
    return redirect('/')

@app.route('/increment1')
def increment1():
    session['inc'] = 1
    return redirect('/')

@app.route('/increment2')
def increment2():
    session['inc'] = 2
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
