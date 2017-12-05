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
    game1= Game(name="Wii Sports",platform='Wii',year_of_release='2006',genre='Sports',description='11',publisher=publisher1)
    game2= Game(name="Just Dance",platform='Wii',year_of_release='2011',genre='Misc',description='22',publisher=publisher2)
    game3= Game(name="Gran Turismo 5",platform='PS3',year_of_release='2010',genre='Racing',description='33',publisher=publisher3)
    db.session.add(publisher1)
    db.session.add(publisher2)
    db.session.add(publisher3)
    db.session.add(game1)
    db.session.add(game2)
    db.session.add(game3)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
