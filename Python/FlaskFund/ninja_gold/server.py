from flask import Flask, render_template, request, redirect, session, jsonify
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['gold'] = 0
    session['log'] = ''
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def guessFunc():
    return ('', 204)

@app.route('/process_money/<area>', methods=['POST'])
def reset(area):
    newGold = 0
    log1 = ''
    log2 = ''
    if area == 'farm':
        newGold += random.randint(10,21)
        logEntry = 'You worked{{newGold}} the shit outta that farm for'
    elif area == 'cave':
        newGold += random.randint(5,10)
    elif area == 'house':
        newGold += random.randint(2,5)
    elif area == 'casino':
        newGold += random.randint(-50,50)
    session['log'] += log1 + newGold + log2
    session['gold'] += newGold
    print session['gold']
    #you are working on getting the log to display in html
    return render_template("index.html", newGold=newGold, log1=log1, log2=log2)


# @app.route('/reset')
# def reset():
#     session['counter'] = 0
#     return redirect('/')

app.run(debug=True)
