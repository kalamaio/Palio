from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired



class LoginForm (FlaskForm):
    username = StringField ( 'Username', validators=[DataRequired()])
    password = PasswordField ('Password', validators=[DataRequired()])
    remember_me = BooleanField ('Remembre ME')
    submit = SubmitField ('Login')
    
    
    