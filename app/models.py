from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

        

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    '''
    Class User that defines the tables of the user user database in the database
    '''
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('This password is inaccessible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

    pass_secure = db.Column(db.String(255))

    

class Pitch(db.Model):
    '''
    Class pitch that defines the tables in the pitch database
    '''

    pitch_list = []
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255), index = True)
    comments = db.Column(db.String(255))
    vote_count = db.Column(db.String)
    date_created = db.Column(db.Date, default=datetime.now)

    '''
    Function that saves new;y created pitches
    '''
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    '''
    Class method that shows a list of pitches
    '''
    @classmethod
    def get_pitch(cls, id):
        pitches = Pitch.query.order_by(Pitch.date_posted.desc()).filter_by(category_id=id).all()
        return pitches




class Category(db.Model):
    '''
    Class that defines a table for the different pitch categories
    '''
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key = True)
    details = db.Column(db.String(255))
    name = db.Column(db.String(255))
    pitch = db.relationship("Pitch", backref = "category", lazy="dynamic")

    '''
    Function to save new pitch category
    '''
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    
    '''
    Class method that returns the categories of pitches by querying the database
    '''
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories


class Comments(db.Model):
    '''
    Class Comments for the Comments column
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.Column(db.String(255))
    date_created = db.Column(db.Date, default=datetime.now)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitch.id"))
