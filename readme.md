# BookManager

## This web app is made using django-python

1. Creating Books information (Name, Author, Genre, Language) and storing it to the database
1. Displaying all the books information stored in the database on a webpage.
1. Added the feature to filter the books by genre and language.
3.1 Filtering is made possible by selecting multiple genres and langauges as well.

## MANUAL: -

1. Create a folder and put all the fiels in it.
1. Create a virtual environment using `mkvirtualenv env`.
2.1 Be sure to install the library virtualenv and virtualenvwrapper-win `pip install virtualenv` and `pip install virtualenvwrapper-win`.
1. Activate the virtual env by `activate env`.
1. Install the requirements for your virtual env by `pip install -r requirements.txt`

### Creating a superuser: -

1. After activating the virtual environment type in the terminal `python manage.py createsuperuser`.
1. Then enter the username and password (Email is optional).

### Running the server: -

1. In the virtual environment type `python manage.py runserver`.
1. Then click the link given in the terminal or go to http://127.0.0.1:8000/.

```Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 09, 2021 - 19:30:44
Django version 3.2.4, using settings 'bookmanagement.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.```
