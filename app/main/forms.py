from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    pitch_title =StringField('Pitch title',validators=[Required()])
    category_name = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch'),('Pickup','Pickup Lines')],validators=[Required()])
    text = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    text = TextAreaField('Write a comment:',validators=[Required()])
    submit = SubmitField('Submit')