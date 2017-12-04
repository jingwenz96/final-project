from flask_script import Manager
from videogame import app, db, Publisher, Game

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    publisher1 = Publisher(name="Nintendo", year_founded="1889", location="JP")
    publisher2 = Publisher(name="Ubisoft", year_founded="1986", location="FR")
    publisher3 = Publisher(name="Sony Computer Entertainment", year_founded="1993", location="JP")
    db.session.add(publisher1)
    db.session.add(publisher2)
    db.session.add(publisher3)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
