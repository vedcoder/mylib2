from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
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

class NewBookForm(Form):
    name = StringField('name',validators=[DataRequired("Please enter the name of the book")])
    author = StringField('author',validators=[DataRequired("Please enter the author of the book ")])
    story = StringField('Story line',validators=[DataRequired("Please enter the storyline of the book")])
    price = StringField('price',validators=[DataRequired("Please enter the price of the book")])
    link = StringField('link for amazon website',validators=[DataRequired("Please enter the link to amazon website to buy this product")])
    myChoices=[('read', 'read'), ('not read', 'not read'), ('in progress', 'in progress')]
    status = SelectField('status', choices = myChoices, validators=[DataRequired("Please enter the choice that you have read it or not")])
    submit = SubmitField('add')
