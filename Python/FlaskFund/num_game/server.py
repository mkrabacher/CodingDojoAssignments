from flask import Flask, render_template, request, redirect, session, jsonify
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 101)
        print session['number']
    return render_template("index.html", template='nill')

@app.route('/process', methods=['POST'])
def guessFunc():
    guess = request.form['guess']
    print guess
    print session['number']
    print guess == session['number']
    print guess > session['number']
    print guess < session['number']
    if session['guess'] == session['number']:
        return render_template('index.html', template='winner')
    elif session['guess'] < session['number']:
        return render_template('index.html', template='less')
    elif session['guess'] > session['number']:
        return render_template('index.html', template='greater')
    return ('', 204)

@app.route('/reset', methods=['POST'])
def reset():
    print 'hello'
    session['number'] = random.randint(1, 101)
    return redirect('/')

# @app.route('/reset')
# def reset():
#     session['counter'] = 0
#     return redirect('/')

app.run(debug=True)
