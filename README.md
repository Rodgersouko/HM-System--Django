# Hospital Management System
## Description
This project is an online Hospital Management System that 
seeks to revolutionalize the health system by digitizing 
hospital day-to-day activities e.g booking appointments.

### Author
1. Lekam Charity
2. Susan Kathoniey
3. Dennis Mutai
4. Kennedy Kiptoo
5. Rodgers Ouko

## Front-End link

Click the [ link ](https://github.com/Susan-Kathoni/E-Hospital-Management-System) to view the front-end repository

# Features

A normal authenticated patient can be able to:
  - Sign in to the application to start using it.
  - Set up a profile which contains:
          1. Name 
          2. Email
          3. Gender
          4. Picture
  - Find a list of available doctors and book appointment.
  - Find Contact Information for the emergency services e.g health department.
  - Patient can only book one appointment at a time.

Doctor can be able to:
  - Sign in to the application to start using it.
  - Set up a profile which contains:
          1. Username
          2. Email
          3. Gender
          4. Picture
          5. speciality.
  - Add information about hospital for example: health care services provided.
  - Respond to patient appointment.

The system administrator can be able to:
  - Create users
  - Delete users 
  - Edit users information
  - See all users
  - Change user statuses: Either from users admin to regular user, or the opposite.
  - Remove users.

## Project live site
  This is the live .[ Click for the demo]( https://hmsystem234.herokuapp.com/)

# Technologies Used
- Python.
- Django (Python framework)

# Installation

- Create and activate virtualenv.
- Install required packages: 
- pip install -r backend/requirements.txt.

# Setup

- copy settings.py.txt to settings.py and update the db credentials.(If you are using SQLLite)
- Setup database
- run python manage.py migrate
- Run the server
- Check if the application is running correctly
- Create a superuser for the admin backend
- run python manage.py createsuperuser and input the credentials
- Login as superuser

# Endpoints
Download [ postman]( https://www.postman.com/downloads/ ) to access the following endpoints

- login endpoint (https://hmsystem234.herokuapp.com/api/login/)
- get all users endpoint (https://hmsystem234.herokuapp.com/api/users/)
- user login endpoint (https://hmsystem234.herokuapp.com/api/login/)
- book appointment endpoint (https://hmsystem234.herokuapp.com/api/appointments/)
- view appointment endpoint (https://hmsystem234.herokuapp.com/api/appointments/)
- response to appointment (https://hmsystem234.herokuapp.com/api/response/)




[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]

© [Kiptoo Kennedy](https://github.com/kiptoo097)

