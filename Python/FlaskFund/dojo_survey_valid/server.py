from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'a'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/info', methods=["POST"])
def process():
    print 'POST working...'
    resub = True
    name = request.form['name']
    location = request.form['location']
    fav_lang = request.form['fav_lang']
    comment = request.form['comment']
    if len(name) == 0:
        flash("name can't be empty homie")
        resub = False
    if len(comment) == 0:
        flash("i know comment says 'optional' right there. but no, please fill out a comment.")
        resub = False
    if len(comment) > 120:
        flash("hey we don't need your whole life story. try cutting your comment to the length we very clearly specified.")
        resub = False
    if resub:
        return render_template("info.html", comment=comment, name=name, location=location, fav_lang=fav_lang)
    return render_template("index.html")








app.run(debug=True)