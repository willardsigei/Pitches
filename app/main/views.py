from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches)


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

@main.route('/pitch/newPitch', methods=['POST','GET'])
@login_required
def newPitch():
    pitch = PitchForm()
    if pitch.validate_on_submit():
        pitch_title = pitch.pitch_title.data
        category_name = pitch.category_name.data
        text= pitch.text.data

        #update pitch instance
        newPitch = Pitch(title = pitch_title,category_name =category_name,content =text,user= current_user )

        #save pitch
        newPitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'NEW PITCH'
    return render_template('new_pitch.html',title = title, new_pitch = pitch)