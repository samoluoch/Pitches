from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from ..models import User
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo

class CommentsForm(FlaskForm):
    comments = TextAreaField('Pitch Comments', validators=[Required()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class PitchForm(FlaskForm): #create a class that inherits from FlaskForm class
    category = SelectField('Category', choices =[('technology','technology'),('pickuplines','pickuplines'),('interviewpitches','interviewpitches')],validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')