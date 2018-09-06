from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class New_Pitch:
    '''
    Class pitch that defines the structure of the Pitch Objcet
    '''
    def __init__(self, id, title, statement, vote_count):
        self.id = id
        self.title = title
        self.statement = statement
        self.vote_count = vote_count

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

        

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    '''
    Class User that defines the tables of the user user database in the database
    '''
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

class Pitch(db.Model):
    '''
    Class pitch that defines the tables in the pitch database
    '''
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255), index = True)
    statement = db.Column(db.String(255))
    vote_count = db.Column(db.String)
    date_created = db.Column(db.Date, default=datetime.now)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()



