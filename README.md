## Building a Flask App with Login and Registration Capability

## 1. Create directory
`mkdir <directory>`
`cd <directory`

## 2. Set up a virtual environment
`python -m venv .env`
`source .env/bin/activate`

## 3. Install packages (assume you already have Python and Pip installed)
* `Flask`
* `flask-sqlalchemy`
* `flask-migrate`
* `flask-Login`
* `werkzeug`
* `flask-wtf`
* `wtforms`
* `python-dotenv`


## Create admin files
`touch .gitignore`
`touch README.md`

## Create a subdirectory where the majority of files will go
`mkdir project`


## Create `__init__.py`
touch app/__init__.py

What goes in `__init__.py`?
`login_manager = LoginManager()

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from project import routes, models`


## Create `routes.py`
`touch project/routes.py`

## Set the FLASK_APP environment variable:
`pip3 install python-dotenv`

`touch .flaskenv`

` # .flaskenv
FLASK_APP=app.py
FLASK_ENV=development`

## Configure (you could put this code in `__init.py`)
`touch config.py`

`import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False`

## Create models
`pip3 install werkzeug`
`pip3 install flask-login`
You're going to create a User class (model). It should have the following attributes:
* id (an integer, generated automatically)
* an email (a string, which the user inputs into a form)
* a username (a string, which the user inputs into a form)
* a password_hash (a string, based on the user's input into a form. The werkzeug.security package is used to create a hashed version of the string)
It will also have two methods:
* `__init__`: the arguments passed will be email, username and password.
* check_password: the werkzeug.security package will be used to do this

## Create forms
`touch project/forms.py`

`pip3 install flask-wtf`
`pip3 install wtforms`

LoginForm:
* email
* password
* submit

RegistrationForm:
* email
* username
* password
* password_confirm
* submit



## Create templates for html files
`mkdir project/templates`



## Create static css file(s)
`mkdir project/static`
`mkdir project/static/css`
`touch project/static/css/styles.css`
