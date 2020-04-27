from project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # UserMixin provides defaults for common user methods

# allows flask login to load to user_id and grab their id, so the app can show content relevant to that user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create a User class
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64, unique = True, index = True))
    username = db.Column(db.String(64, unique = True, index = True))
    password_hash = db.Column(db.String(128)) # it's not actually the password, but a hashed version

    # the init function contains the password itself as an argument, which it then hashes
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    # check the password by comparing the password_hash to the password that is given
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
