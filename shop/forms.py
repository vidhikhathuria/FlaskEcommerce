from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=25)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', validators=[DataRequired(), Length(min=4, max=35), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

class LoginForm(Form):
    email = StringField('Email Address', validators=[DataRequired(), Length(min=4, max=35), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    