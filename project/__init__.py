import os
from flask import Flask

# from flask import Flask, render_template, url_for, redirect, flash

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask import flask_login
from flask_login import LoginManager

## create an instance of LoginManager
login_manager = LoginManager()

## create the app
app = Flask(__name__)

## configs
app.config['SECRET_KEY'] = 'mykey'

################################
##### SQL DATABASE SECTION #####

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

# it's important that the import of routes is done after the app = Flask(__name__) line
from project import routes

## pass the app to the loginManager
login_manager.init_app(app)
login_manager.login_view = 'login' # this will be one of the views (routes)





########### TAKE ONE ##############

# from flask import Flask, render_template, url_for, redirect, flash
# from flask import Flask
#
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from config import Config
#
#
# ## create the app
# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# Migrate(app,db)
#
# ## is this import needed?
# # from app import routes, models
#
#
# ## create an instance of LoginManager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login' # this will be one of the views (routes)
