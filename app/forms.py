from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms.fields import TextField, FileField, SelectField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import Form

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])



class ProfileForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    age = IntegerField('Age', validators=[Required()])
    sex = SelectField('Sex', choices=[('Male', 'Male'), ('Female','Female')], validators=[Required()])
    image = FileField('Profile Photo', validators=[FileRequired(), FileAllowed(['jpg,png'], 'Images Only!')])
    biography = TextField('Biography', validators=[Required()])