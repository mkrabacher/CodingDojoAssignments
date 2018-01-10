from flask import Flask, render_template

port_app = Flask(__name__)

@port_app.route('/')
def index():
    return render_template('index.html')

@port_app.route('/projects')
def projects():
    return render_template('projects.html')

@port_app.route('/about')
def about():
    return render_template('about.html')

port_app.run(debug=True)