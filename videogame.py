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

# Publisher Page
@app.route('/publishers')
def publishers():
    publishers = Publisher.query.all()
    return render_template('publishers.html', publishers=publishers)

@app.route('/publisher/add', methods=['GET', 'POST'])
def add_publishers():
    if request.method == 'GET':
        return render_template('publisher-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        location = request.form['location']
        year_founded = request.form['year_founded']
        # insert the data into the database
        publisher = Publisher(name=name, location=location, year_founded=year_founded)
        db.session.add(publisher)
        db.session.commit()
        return redirect(url_for('publishers'))

@app.route('/publisher/edit/<int:id>', methods=['GET', 'POST'])
def edit_publisher(id):
    publisher = Publisher.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('publisher-edit.html', publisher=publisher)
    if request.method == 'POST':
        # update data based on the form data
        publisher.name = request.form['name']
        publisher.location = request.form['location']
        publisher.year_founded = request.form['year_founded']
        # update the database
        db.session.commit()
        return redirect(url_for('publishers'))

@app.route('/publisher/delete/<int:id>', methods=['GET', 'POST'])
def delete_publisher(id):
    publisher = Publisher.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('publisher-delete.html', publisher=publisher)
    if request.method == 'POST':
        db.session.delete(publisher)
        db.session.commit()
        return redirect(url_for('publishers'))

# Game Page
@app.route('/games')
def games():
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
        return redirect(url_for('games'))


@app.route('/game/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    game = Game.query.filter_by(id=id).first()
    publishers = Publisher.query.all()
    if request.method == 'GET':
        return render_template('game-edit.html', game=game, publishers=publishers)
    if request.method == 'POST':
        # update data based on the form data
        game.name = request.form['name']
        game.platform = request.form['platform']
        game.year_of_release = request.form['year_of_release']
        game.genre = request.form['genre']
        game.description = request.form['description']
        publisher = Publisher.query.filter_by(name=publisher_name).first()
        game.publisher = publisher
        # update the database
        db.session.commit()
        return redirect(url_for('games'))


@app.route('/game/delete/<int:id>', methods=['GET', 'POST'])
def delete_game(id):
    game = Game.query.filter_by(id=id).first()
    publishers = Publisher.query.all()
    if request.method == 'GET':
        game=Game.query.filter_by(id=id).first()
        return render_template('game-delete.html', game=game, publishers=publishers)
    if request.method == 'POST':
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('games'))

if __name__ == '__main__':
    app.run(debug=True)
