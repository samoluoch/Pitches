from flask import render_template
from . import main
from .. import db
from ..models import Pitch

# Views
@main.route('/')
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''
    # interviews = Pitch.query.get('interviews)
    # inspirational = get_pitch('inspirational')
    # general = get_pitch('general')



    title = 'Welcome to the Pitch Page'
    return render_template('index.html', title=title)

@main.route('/pitch/<int:id>')
def pitch(id):
    '''
    View pitch function that returns the details of the pitch as well as enable the reation of a comment
    '''
    pitch = Pitch.query.get(id)

    title = 'Welcome to the Pitch Page'

    if pitch is None:
        abort(404)

    comment =  Comments.get_comments(id)
    
    return render_template('pitch.html', title=title)




