from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SignupForm(Form):
    firstname = StringField('First name',validators=[DataRequired("Please enter first name")])
    lastname = StringField('Last name',validators=[DataRequired("Please enter last name")])
    email = StringField('Email',validators=[DataRequired("Please enter email"),Email("Please enter your email address.")])
    password = PasswordField('Password',validators=[DataRequired("Please enter Password"),Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')

class EditAccountForm(Form):
    firstname = StringField('First name',validators=[DataRequired("Please enter first name")])
    lastname = StringField('Last name',validators=[DataRequired("Please enter last name")])
    email = StringField('Email',validators=[DataRequired("Please enter email"),Email("Please enter your email address.")])
    submit = SubmitField('Sign up')


class ChangePasswordForm(Form):
    oldpassword = PasswordField('Old Password',validators=[DataRequired("Please enter your Old Password"),Length(min=6, message="Passwords must be 6 characters or more.")])
    newpassword = PasswordField('New Password',validators=[DataRequired("Please enter your New Password"),Length(min=6, message="Passwords must be 6 characters or more.")])
    confirmpassword = PasswordField('Confirm Password',validators=[DataRequired("Please comfirm your Password"),Length(min=6, message="Passwords must be 6 characters or more."),EqualTo('newpassword',message="password must match")])
    submit = SubmitField('Change Password')


class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class NewBookForm(Form):
    name = StringField('Name',validators=[DataRequired("Please enter the name of the book(full name)")])
    author = StringField('Author',validators=[DataRequired("Please enter the author of the book ")])
    story = StringField('Story line',validators=[DataRequired("Please enter the storyline of the book")])
    link = StringField('Amazon link',validators=[DataRequired("Please enter the link to amazon website to buy this product")])
    price = StringField('Price',validators=[DataRequired("Please enter the price of the book")])
    submit = SubmitField('Add')

class NewToyForm(Form):
    name = StringField('Name',validators=[DataRequired("Please enter the name of the toy(full name)")])
    brand = StringField('Brand',validators=[DataRequired("Please enter the brand of the toy ")])
    description = StringField('Description',validators=[DataRequired("Please enter some description of the toy(about 50 words)")])
    link = StringField('Amazon link',validators=[DataRequired("Please enter the link to amazon website to buy this product")])
    price = StringField('Price',validators=[DataRequired("Please enter the price of the toy")])
    submit = SubmitField('Add')
