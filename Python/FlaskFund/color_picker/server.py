from flask import Flask, url_for, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ninja')
def process():
    ninja_color = 'tmnt.png'
    url = "url_for('static', filename='img/" + ninja_color + "')"
    print url
    return render_template("ninja.html", img_url=url)

@app.route('/ninja/<color>')
def show_dif_ninja(color):
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
    url = "url_for('static', filename='img/" + ninja_img + "')"
    return render_template('ninja.html', ninja_img=ninja_img, ninja_name=ninja_name)








app.run(debug=True)