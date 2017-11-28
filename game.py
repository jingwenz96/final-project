import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET KEY'] = "33445566789"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def member():
    return render_template('members.html')

@app.route('/games')
def games():
    return render_template('games.html')

if __name__ == '__main__':
    app.run(debug=True)
