## Group Final Project: Video Game Database

#### Contents for this Database:

- Two Tables: Game, Publisher

- Relationship: A game can only be published by one publisher; A Publisher can publish many games.

- Game: GameID, Name, Platform, Genre (4 columns)

- Publisher: PublisherID, Name, Location (3 columns)

#### Setup Instructions:

Install `virtualenv` if needed.

1. Activate the virtual environment
    `$ source venv/bin/activate`

2. Install packages needed for this project:
    `$ pip install -r requirements.txt`

3. Initialize the database:
    `$ python manage.py deploy`

4. To run the development server (use `-d` after `runserver` to enable debugger and reloader):
    `$ python manage.py runserver`
