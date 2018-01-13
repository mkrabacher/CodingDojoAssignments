from flask import Flask, render_template, request, redirect, session, jsonify
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['gold'] = 0
    session['log'] = []
    return render_template("index.html", log=session['log'])

@app.route('/process', methods=['POST'])
def guessFunc():
    return ('', 204)

@app.route('/process_money/<area>', methods=['POST'])
def reset(area):
    newGold = 0
    log = session['log']
    log1 = ''
    log2 = ''
    if area == 'farm':
        newGold += random.randint(10,21)
        log1 = 'You worked the shit outta that farm for '
        log2 = ' gold.('
    elif area == 'cave':
        newGold += random.randint(5,10)
        log1 = 'You fell over in the cave and hit your head on '
        log2 = ' gold.('
    elif area == 'house':
        newGold += random.randint(2,5)
        log1 = 'as a wealthly landowner, have '
        log2 = ' gold.('
    elif area == 'casino':
        newGold += random.randint(-50,50)
        if newGold == 0:
            log1 = 'whoa, you barely even got your money back from that dice toss'
        elif newGold > 0:
            log1 = 'you rolled them dice and won '
            log2 = ' gold.('
        elif newGold < 0:
            log1 = 'you rolled them dice and '
            log2 = ' gold. LOSER!('

    if len(log) > 8:
        log.pop(0)
    
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    session['log'].append(log1 + str(newGold) + log2 + st +')')
    session['gold'] += newGold
    return render_template("index.html", newGold=newGold, log=session['log'])


# @app.route('/reset')
# def reset():
#     session['counter'] = 0
#     return redirect('/')

app.run(debug=True)
