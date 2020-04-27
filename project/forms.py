from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Email, EqualTo
from wtforms import ValidationError


# LoginForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')


# RegistrationForm
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = PasswordField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('password_confirm', message = "Your passwords don't match")])
    password_confirm = PasswordField('Confirm your password', validators = [DataRequired()])
    submit = SubmitField('Register')
