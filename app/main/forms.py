from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from ..models import User
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo

class CommentsForm(FlaskForm):
    title = StringField('Comments title', validators=[Required()])
    comments = TextAreaField('Pitch Comments', validators=[Required()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class PitchForm(FlaskForm): #create a class that inherits from FlaskForm class
    name = StringField('Submitted By', validators = [Required()])
    categoy = TextAreaField('Pitch', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')