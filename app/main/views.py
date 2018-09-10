from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from .. import db
from ..models import User, Pitch, Comment
from flask_login import login_required
from flask_login import login_required, current_user
from .forms import CommentsForm,PitchForm

# Views
@main.route('/')
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''
    form = PitchForm()

    if form.validate_on_submit():
        new_pitch = Pitch(actual_pitch=form.pitch.data,category=form.category.data, user_id=current_user.id)
        new_pitch.save_pitch()
        flash('Pitch successfully saved')
    pitch = Pitch.query.filter_by(category='technology')
    
    pickuplines = Pitch.query.filter_by(category='pickuplines')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,pickuplines=pickuplines)

# @main.route('/pitch')
# def pitch():
#     '''
#     View pitch function that returns the details of the pitch as well as enable the reation of a comment
#     '''
#     pitch = Pitch.query.filter_by(category='technology')

#     title = 'Welcome to the Pitch Page'

#     if pitch is None:
#         abort(404)

    
#     return render_template('pitch.html', title=title,pitch=pitch)

# @main.route('/category/pitch/new/', methods=['GET', 'POST'])

@main.route('/pitch/comments/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    pitch = Comment.query.filter_by(pitch_id=id).all()
    if form.validate_on_submit():

        # Updated review instance
        new_comment = Comment(pitch_id=id, comments=form.comments.data)

        # save review method
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.category'))
    title = ' comment'
    return render_template('new_comment.html',title = title, comment_form=form, pitchs=pitch)

@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def comment(id):
    form = CommentsForm()
    pitch = Comment.query.filter_by(pitch_id=id).all()
    if form.validate_on_submit():

        # Updated review instance
        new_comment = Comment(pitch_id=id, comments=form.comments.data)

        # save review method
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.index'))
    title = ' comment'
    return render_template('comments.html',title = title, comment_form=form, pitchs=pitch)


@main.route('/category', methods=['GET', 'POST'])
def category():
    '''
    Function that validates the Pitch form
    '''
    form = PitchForm()

    if form.validate_on_submit():
        new_pitch = Pitch(actual_pitch=form.pitch.data,category=form.category.data, user_id=current_user.id)
        new_pitch.save_pitch()
        flash('Pitch successfully saved')
    pitch = Pitch.query.filter_by(category='technology')
    
    pickuplines = Pitch.query.filter_by(category='pickuplines')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,pickuplines=pickuplines)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

