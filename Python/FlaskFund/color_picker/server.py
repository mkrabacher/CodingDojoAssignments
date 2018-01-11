from flask import Flask, url_for, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    return render_template("index.html", red=red, blue=blue, green=green)






app.run(debug=True)