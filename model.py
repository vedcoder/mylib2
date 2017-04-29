from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(50))
  lastname = db.Column(db.String(400))
  email = db.Column(db.String(120), unique = True)
  pwdhash = db.Column(db.String(180))
  mobile = db.Column(db.String(20))
  society = db.Column(db.String(100))
  tower = db.Column(db.String(10))
  flat = db.Column(db.String(10))

  def __init__(self, firstname, lastname, email, password, mobile, society, tower, flat):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
    self.mobile = mobile.title()
    self.society = society.title()
    self.tower = tower.title()
    self.flat = flat.title()


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
  new_price = db.Column(db.Numeric(precision=5, scale=2))  
  price = db.Column(db.Numeric(precision=5, scale=2))
  link = db.Column(db.String(400))
  image = db.Column(db.String(400))
  #is_sold = db.Column(Boolean, unique=False, default=False)

  def __init__(self, name, author, story, new_price, price, link, image,):
    self.name = name
    self.author = author
    self.story = story
    self.new_price = new_price
    self.price = price
    self.link = link
    self.image = image
   # self.is_sold = is_sold

class Toy(db.Model):
  __tablename__ = 'toys'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50))
  brand = db.Column(db.String(50))
  description = db.Column(db.String(500))
  new_price = db.Column(db.Numeric(precision=5, scale=2))    
  price = db.Column(db.Numeric(precision=5, scale=2))
  link = db.Column(db.String(400))
  image = db.Column(db.String(400))


  def __init__(self, name, brand, description, price, link, image):
    self.name = name
    self.brand = brand
    self.description = description
    self.new_price = new_price    
    self.price = price
    self.link = link
    self.image = image
