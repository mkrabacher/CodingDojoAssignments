from flask import Flask, render_template, request, redirect, session, jsonify
import random
app = Flask(__name__)
app.secret_key = 'a'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 101)
        print session['number']
    return render_template("index.html", template='nill')

@app.route('/process', methods=['POST'])
def guessFunc():
    guess = request.form['guess']
    try:
        if int(guess) == session['number']:
            message = str(session['number']) + 'was the number'
            return render_template('index.html', template='winner', message=message)
        elif int(guess) < session['number']:
            message = 'Too Low!'
            return render_template('index.html', template='less', message=message)
        elif int(guess) > session['number']:
            message = 'Too High!'
            return render_template('index.html', template='greater', message=message)
    except(ValueError):
        pass
    message = 'just put a number in man.'
    return render_template('index.html', template='fail', message=message)

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
