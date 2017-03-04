from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('first name',validators=[DataRequired("Please enter first name")])
    last_name = StringField('last name',validators=[DataRequired("Please enter last name")])
    email = StringField('Email',validators=[DataRequired("Please enter email"),Email("Please enter your email address.")])
    password = PasswordField('Password',validators=[DataRequired("Please enter Password"),Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")
