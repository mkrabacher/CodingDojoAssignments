from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/info', methods=["POST"])
def process():
    print 'POST working...'
    name = request.form['name']
    location = request.form['location']
    fav_lang = request.form['fav_lang']
    return render_template("info.html", name=name, location=location, fav_lang=fav_lang)








app.run(debug=True)