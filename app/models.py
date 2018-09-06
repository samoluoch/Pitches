from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch:
    '''
    Class pitch that defines the structure of the Pitch Objcet
    '''
    def __init__(self, id, title, statement, vote_count):
        self.id = id
        self.title = title
        self.statement = statement
        self.vote_count = vote_count

class User(UserMixin, db.Model):
    '''
    Class User that defines the columns of the user user database in the database
    '''
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")