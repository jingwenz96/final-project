## Group Final Project: Video Game Database

#### Contents for this Database:

- Two Tables: Game, Publisher

- Relationship: A game can only be published by one publisher; A Publisher can publish many games.

- Game: GameID, Name, Platform, Year_of_release, Genre, Description, PublisherID(FK) (7 columns)

- Publisher: PublisherID(PK), Name, Location (3 columns)

#### Process:
- [x] Database Setup
- [ ] Complete Table contents
- [x] Members Photo
- [x] Add
- [ ] Edit
- [ ] Delete

#### Setup Instructions:

Install `virtualenv` if needed.

1. Activate the virtual environment
    `$ source venv/bin/activate`

2. Install packages needed for this project:
    `$ pip install -r requirements.txt`

#### Run Project with prebuilt database:
1. Initialize the database:
    `$ python manage.py deploy`

2. To run the development server (use `-d` after `runserver` to enable debugger and reloader):
    `$ python manage.py runserver`
