from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(50))
  lastname = db.Column(db.String(400))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(180))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

class Book(db.Model):
  __tablename__ = 'books'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50))
  author = db.Column(db.String(50))
  story = db.Column(db.String(100))
  price = db.Column(db.Numeric(precision=5, scale=2))
  link = db.Column(db.String(400))
  image = db.Column(db.String(400))

  def __init__(self, name, author, story, price, link, image ):
    self.name = name
    self.author = author
    self.story = story
    self.price = price
    self.link = link
    self.image = image

class Toy(db.Model):
  __tablename__ = 'toys'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50))
  brand = db.Column(db.String(50))
  description = db.Column(db.String(500))
  price = db.Column(db.Numeric(precision=5, scale=2))
  link = db.Column(db.String(400))
  image = db.Column(db.String(400))


  def __init__(self, name, brand, description, price, link, image):
    self.name = name
    self.brand = brand
    self.description = description
    self.price = price
    self.link = link
    self.image = image