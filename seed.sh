#!/bin/bash
rm -rf cozynestapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations cozynestapi
python manage.py migrate cozynestapi
python manage.py loaddata users
python manage.py loaddata rooms
python manage.py loaddata pieces
python manage.py loaddata styles
python manage.py loaddata piecestyles

# Run "chmod +x seed.sh" in the terminal.
# run "./seed.sh" in the terminal to run the commands
