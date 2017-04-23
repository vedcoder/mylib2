from flask import Flask, render_template, request, session, redirect, url_for
from model import db, User, Book, Toy
from forms import SignupForm, LoginForm, NewBookForm, NewToyForm, EditAccountForm, ChangePasswordForm, EditBookForm, EditToyForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/mylib'

db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/books")
def books():
  books = db.session.query(Book).all()
  return render_template("books.html",books=books)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
      return redirect (url_for("account"))
  form = SignupForm()
  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      user = User.query.filter_by(email=form.email.data).first()
      if user is not None:
        print("user is in i don't know",user.email)
        return render_template('signup.html', form=form, error="user already exists")
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data, form.mobile.data, form.society.data, form.tower.data, form.flat.data)
      db.session.add(newuser)
      db.session.commit()
      return redirect(url_for('login'))

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
  else:
      user = User.query.filter_by(email=session['email']).first()
      return render_template("account.html",user=user)

@app.route("/newbook",methods=["GET", "POST"])
def newbook():
    form = NewBookForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("newbook.html", form=form)
        else:
            newbook = Book(form.name.data, form.author.data, form.story.data, form.price.data, form.link.data, form.image.data)
            db.session.add(newbook)
            db.session.commit()
            return redirect(url_for('books'))
    elif request.method == "GET":
        return render_template("newbook.html",form=form)

@app.route("/editbook", methods=["GET", "POST"])
def editbook():
  if 'email' in session:
      print("in el")
      form = EditBookForm()
      if request.method == "POST":
        if form.validate() == False:
          return render_template('editbook.html', form=form)
        else:
          id = form.id.data
          book = Book.query.filter_by(id=id).first()
          book.name=form.name.data
          book.author=form.author.data
          book.story=form.story.data
          book.price=form.price.data
          book.link=form.link.data
          book.image=form.image.data
          db.session.commit()
          return redirect(url_for('books'))
      elif request.method == "GET":
        book = Book.query.filter_by(id=request.args['id']).first()
        form = EditBookForm(obj=book)
        return render_template("editbook.html",form=form)
  else:
      return redirect (url_for("login"))        

@app.route("/newtoy",methods=["GET", "POST"])
def newtoy():
    form = NewToyForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("newtoy.html", form=form)
        else:
            newtoy = Toy(form.name.data, form.brand.data, form.description.data, form.price.data, form.link.data, form.image.data)
            db.session.add(newtoy)
            db.session.commit()
            return redirect(url_for('toys'))
    elif request.method == "GET":
        return render_template("newtoy.html",form=form)

@app.route("/edittoy", methods=["GET", "POST"])
def edittoy():
  if 'email' in session:
      form = EditToyForm()
      if request.method == "POST":
        if form.validate() == False:
          return render_template('edittoy.html', form=form)
        else:
          id = form.id.data
          toy = Toy.query.filter_by(id=id).first()
          toy.name=form.name.data
          toy.brand=form.brand.data
          toy.description=form.description.data
          toy.price=form.price.data
          toy.link=form.link.data
          toy.image=form.image.data
          db.session.commit()
          return redirect(url_for('toys'))
      elif request.method == "GET":
        toy = Toy.query.filter_by(id=request.args['id']).first()
        form = EditToyForm(obj=toy)
        return render_template("edittoy.html",form=form)
  else:
      return redirect (url_for("login"))             

@app.route("/toys")
def toys():
  toys = db.session.query(Toy).all()
  return render_template("toys.html",toys=toys)

@app.route("/editaccount", methods=["GET", "POST"])
def editaccount():
  if 'email' in session:
      user = User.query.filter_by(email=session['email']).first()
      form = EditAccountForm(obj=user)
      if request.method == "POST":
        if form.validate() == False:
          return render_template('editaccount.html', form=form)
        else:
           user.email=form.email.data
           user.firstname=form.firstname.data
           user.lastname=form.lastname.data
           user.mobile=form.mobile.data
           user.society=form.society.data
           user.tower=form.tower.data
           user.flat=form.flat.data

           db.session.commit()
           session['email'] = form.email.data
           return redirect(url_for('account'))
      elif request.method == "GET":
        return render_template("editaccount.html",form=form)
  else:
      return redirect (url_for("login"))

@app.route("/changepassword", methods=["GET", "POST"])
def changepassword():
  error=None
  if 'email' in session:
      user = User.query.filter_by(email=session['email']).first()
      form = ChangePasswordForm()
      if request.method == "POST":
        if form.validate() == False:
          return render_template('changepassword.html', form=form)
        else:
          oldpassword = form.oldpassword.data
          newpassword = form.newpassword.data
          if user is  None or not user.check_password(oldpassword):
              error="check your old password"
              return render_template('changepassword.html', form=form, error=error)
          else:
             user.password = newpassword
             db.session.commit()
             return redirect (url_for("account"))
      elif request.method == "GET":
        return render_template("changepassword.html",form=form)
  else:
      return redirect (url_for("login"))


if __name__ == "__main__":
  app.run(debug=True)
