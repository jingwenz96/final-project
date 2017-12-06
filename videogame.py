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
    description = db.Column(db.Text)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def member():
    return render_template('members.html')

@app.route('/games')
def game():
    games = Game.query.all()
    return render_template('games.html',games=games)


@app.route('/game/add', methods=['GET', 'POST'])
def add_games():
    if request.method == 'GET':
        publishers = Publisher.query.all()
        return render_template('game-add.html', publishers=publishers)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        platform = request.form['platform']
        year_of_release = request.form['year_of_release']
        genre = request.form['genre']
        description = request.form['description']
        publisher_name = request.form['publisher']
        publisher = Publisher.query.filter_by(name=publisher_name).first()
        game = Game(name=name, platform=platform, year_of_release=year_of_release, genre=genre, description=description, publisher=publisher)

        # insert the data into the database
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('game'))

'''
@app.route('/game/delete/<int:id>', methods=['GET', 'POST'])
def delete_game(id):
    game = Game.query.filter_by(id=id).first()
    publishers = Publisher.query.all()
    if request.method == 'GET':
        return render_template('game-delete.html', game=game, publishers=publishers)
    if request.method == 'POST':
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('game')
'''
@app.route('/publishers')
def publisher():
    publishers = Publisher.query.all()
    return render_template('publisher.html', publishers=publishers)


@app.route('/publisher/add', methods=['GET', 'POST'])
def add_publisher():
    if request.method == 'GET':
        return render_template('publisher-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year_founded = request.form['year_founded']
        location = request.form['location']
        # insert the data into the database
        publisher = Publisher(name=name, year_founded=year_founded,location=location)
        db.session.add(publisher)
        db.session.commit()
        return redirect(url_for('publisher'))

'''
@app.route('/publisher/delete/<int:id>', methods=['GET', 'POST'])
def delete_publisher(id):
    publisher = Publisher.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('publisher-delete.html', publisher=publisher)
    if request.method == 'POST':
        db.session.delete(publisher)
        db.session.commit()
        return redirect(url_for('publisher'))
'''

if __name__ == '__main__':
    app.run(debug=True)
