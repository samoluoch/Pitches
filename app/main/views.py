from flask import render_template
from . import main
# from .. import db
# from ..models import Pitch

# Views
@main.route('/')
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''

    title = 'Welcome to the Pitch Page'
    return render_template('index.html', title=title)

# @main.route('/pitch/<int:id>')
# def pitch(id):
#     '''
#     View pitch function that returns the details of the pitch
#     '''
#     # pitch = Pitch.get_pitches.get(id)

#     title = 'Welcome to the Pitch Page'
    
#     return render_template('pitch.html', title=title)



