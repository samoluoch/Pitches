from flask import render_template
from . import main
from .. import db

# Views
@main.route('/')
def index():
    '''
    View page function that returns the details on the index page
    '''

    title = 'Welcome to the Pitch Page'
    return render_template('index.html', title=title)




