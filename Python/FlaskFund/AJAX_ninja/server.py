from flask import Flask, url_for, render_template, request, redirect, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/ninja', methods=['POST'])
# def getApril():
#     return jsonify(ninja='static\img\\notapril.png', quote="Man, what a great choice she was")

@app.route('/ninja/<color>')
def json_response(color):
    print color
    ninja_img = 'notapril.jpg'
    if color == 'red':
        ninja_img = 'raphael.jpg'
        ninja_name = "Look Out! Raph's comin' atcha!"
    elif color == 'blue':
        ninja_img = 'leonardo.jpg'
        ninja_name = "leo shaving his dome while doing yoga. #justturtlethings"
    elif color == 'orange':
        ninja_img = 'michelangelo.jpg'
        ninja_name = "mikie's got 4 sticks attached with chains. remember bruce lee?"
    elif color == 'purple':
        ninja_img = 'donatello.jpg'
        ninja_name = "I HAZ A STICK. IT GUUUUD."
    else:
        ninja_name = "Man, what a great choice she was"

    # url = "url_for('static', filename='img/" + ninja_img + "')"
    return jsonify(ninja='static\img\\'+ninja_img, quote=ninja_name)






app.run(debug=True)