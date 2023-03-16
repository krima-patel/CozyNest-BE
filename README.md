# 🏠 Cozy Nest: Server Side 🏠
## Purpose and Target Audience
Cozy Nest is an interior design and decor application providing users structure when it comes to designing their space. Designing a new space or renovating an existing one is exciting, but people can oftentimes easily become inundated with the myriad of ideas and inspirations. This is where Cozy Nest comes in! You can add the specific rooms you want to design and the pieces you want in your rooms. This allows the user to keep an account of the rooms and pieces, while also being able to visualize the room and the associated pieces. This streamlines the home design process, giving users more clarity and peace of mind.

## Primary Features of Cozy Nest

- Google Authentication is required to gain access to Cozy Nest
- Upon authentication, new user will be shown a form to fill out before accessing contents of the application
- Landing page will provide users with images and descriptions of the 18 most popular interior design styles, allowing users to better determine what styles they may want to incorporate into their spaces
- Public view - all authenticated users can view rooms and pieces created by other authenticated users
- Authenticated users are able to create their a room/space
- Authenticated users are able to submit a piece(s) that accompanies a particular room
- Authenticated users are able to edit and delete rooms they have created, but can only view rooms created by other authenticated users
- Authenticated users are able to create a piece they would like to share
- Authenticated users are able to select one room they would like a piece to belong to. The room they select will be a room they have created, not a room created by another authenticated user.
- Authenticated users are able to edit and delete pieces they have created and shared, but can only view pieces created by other authenticated users
- Users are able to sign out of the application via the "Sign Out" button on the nav bar

## Check out Cozy Nest! Run on your local machine:
These are the server side instructions for this application:
1. Clone CozyNest-BE to your local machine
git@github.com:krima-patel/CozyNest-BE.git
2. Navigate into the CozyNest-BE directory:
cd CozyNest-BE
3. Initialize a new virtual environment by running this command:
pipenv shell
4. Install the third party packages:
pipenv install django autopep8 pylint djangorestframework django-cors-headers pylint-django
5. Make your migrations:
python manage.py makemigrations cozynestapi
python manage.py migrate
6. Seed the database with some sample data you can work with:
A quick and easy way to do this:
- Create a seed.sh file at the root of the project (should not be in any other folder within the project, it should be outside/be its own file)
- Add the following commands to the seed.sh file:
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
- Run these commands by running two commands:
First, run "chmod +x seed.sh"
Then run "./seed.sh"
7. Now start your API server! Run this command:
python manage.py runserver


## Begin Designing Your Own Cozy Nest!

- Begin by clicking "Sign In". You will be presented with a form, asking for your name (this can be anything you want), an image (again, anything you want), and your design bio
- After submitting the form, you will come to the landing page, "What's Your Style?" page
- The Browse Rooms page allows authenicated users to view rooms users are designing
- When viewing a single room, all authenticated users are able to view the pieces and details pertaining to that specific room
- The Browse Pieces page allows authenicated users to view pieces users are sharing
- Add a Room is a form that asks users about the room they are designing
- Share a Piece is a form that asks users information about a piece they want to share and put in a particular room that was created by the logged in authenticated user

## Planning for the project:
- [Cozy Nest ERD](https://dbdiagram.io/d/63de819e296d97641d7e7174)
- [Cozy Nest Wireframe](https://whimsical.com/krima-s-cozynest-wireframe-GuLoPWBKnZSPUK3dahrGRd)

## Contributions

Krima Patel
- [Krima's LinkedIn](https://www.linkedin.com/in/krima-patel/)
- Krima's email: patel.krima@hotmail.com

## Backend Tech Stacks:
<img height=50 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/><img height=50/>
<img height=50 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django.svg"/><img height=50/>
<img height=50 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original-wordmark.svg"/><img height=50/>
          
          
