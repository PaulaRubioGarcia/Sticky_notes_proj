## Prerequisites
Ensure you have the following installed:

Python 3.x
pip (Python package installer)
Virtualenv (optional but recommended)
Step-by-Step Guide



### Setup Instructions
Follow these steps to set up the project on your local machine:

# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


# Install dependencies:
pip install -r requirements.txt


# Apply migrations:
python manage.py migrate

Create a superuser:


# Run the development server:
python manage.py runserver

Open your web browser and navigate to http://127.0.0.1:8000/ to see the application in action.


## 1. Set Up the Project
## Install Django:
pip install django


# Create a Django Project:
django-admin startproject sticky_notes_proj
cd sticky_notes_project


# Create a Django App:
python manage.py startapp notes_app


## 2.Define Models
In notes/models.py, define the Note and Post models:
(Look models.py file in notes_app folder)


##3.Create and Apply Migrations
Run the following commands to create and apply migrations:
python manage.py makemigrations
python manage.py migrate


##4.Create Forms
In notes/forms.py, create forms for Note and Post:
(Look forms.py file in notes_app folder)


##5.Create Views
In notes/views.py, create views for handling CRUD operations:
(Look views.py file in notes_app folder)


##6.Templates
Create HTML templates for displaying and managing notes and posts.
(Look on the folder notes_app and the folder templates, to see the HTML you need to create)

****Static Files and CSS*****
Add Bootstrap for styling and a custom CSS file for additional styles:
(Look at the folder statics inside notes_app folder, and look at the style.css file)


##7.URLs
Add URL configurations for notes and posts in notes/urls.py:
(Looks at urls.py in notes_app folder to see the structure)


**Update the main URL configuration in sticky_notes_project/urls.py:**
(Look inside sticky_notes_proj folder in urls.py file to see the strcture)


##8.Tests
Write tests to ensure the functionality of your application in notes/tests.py:
(Look in test.py file inside notes_app folder to see the strcture)(You might have to create the file)



###Run the development server:
python manage.py runserver


##Access the application:
Open your browser and go to http://127.0.0.1:8000/.
