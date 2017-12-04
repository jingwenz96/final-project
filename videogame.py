import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# define database tables
class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.CHAR(2))
    year_founded = db.Column(db.Integer)
    publisher = db.relationship('Game', backref='publisher', cascade='delete')

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    platform = db.Column(db.String(64))
    year_of_release = db.Column(db.Integer)
    genre = db.Column(db.String(64))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def member():
    return render_template('members.html')

@app.route('/games')
def game():
    return render_template('games.html')

@app.route('/publisher')
def publisher():
    return render_template('publisher.html')



if __name__ == '__main__':
    app.run(debug=True)
