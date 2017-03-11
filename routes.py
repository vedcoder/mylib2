from flask import Flask, render_template, request, session, redirect, url_for
from model import db, User, Book
from forms import SignupForm, LoginForm, NewBookForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/mylib'

db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/books")
def books():
  return render_template("books.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
      return redirect (url_for("account"))
  form = SignupForm()
  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('account'))

  elif request.method == "GET":
    return render_template("signup.html",form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
      return redirect (url_for("account"))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data
      password = form.password.data

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        session['fname'] = firstname
        session['lname'] = lastname

        return redirect(url_for('account'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route("/account")
def account():
  if 'email' not in session:
      return redirect (url_for("login"))
  return render_template("account.html")

@app.route("/newbook",methods=["GET", "POST"])
def newbook():
    form = NewBookForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("newbook.html", form=form)
        else:
            newbook = Book(form.name.data, form.author.data, form.story.data, form.price.data, form.link.data)
            db.session.add(newbook)
            db.session.commit()
            return redirect(url_for('books'))
    elif request.method == "GET":
        return render_template("newbook.html",form=form)

if __name__ == "__main__":
  app.run(debug=True)
