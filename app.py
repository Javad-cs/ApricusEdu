from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import time

db = SQL("sqlite:///project.db")

# Configure session to use filesystem (instead of signed cookies)

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html",message1="*must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            username = request.form.get("username")
            return render_template("login.html",message1="", message2="*must provide password", username=username)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            username = request.form.get("username")
            return render_template("login.html", message1="*invalid username and/or password", message2="", username=username)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return render_template("index1.html")
    else:
        return render_template("login.html")

@app.route("/gotologin", methods=["GET", "POST"])
def gotologin():
    if request.method == "POST":
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/gotosignup", methods=["GET", "POST"])
def gotosignup():
    if request.method == "POST":
        return render_template("signup.html")
    else:
        return render_template("signup.html")

@app.route("/gohome", methods=["GET", "POST"])
def gohome():
    if request.method == "POST":
        return render_template("index.html")
    else:
        return render_template("index.html") 

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not name:
            a = "must provide name"
            return render_template("signup.html", message1=a, name=name, surname=surname, username=username)
        elif not surname:
            return render_template("signup.html", message2="*must provide surname", name=name, surname=surname, username=username)
        elif not username:
            return render_template("signup.html", message3="*must provide username", name=name, surname=surname, username=username)
        elif len(rows) != 0:
            return render_template("signup.html", message3="*there already exists such username", name=name, surname=surname, username=username)
        elif not password:
            return render_template("signup.html", message4="*must provide password", name=name, surname=surname, username=username)
        elif not confirmation:
            return render_template("signup.html", message5="*confirm the password", name=name, surname=surname, username=username)
        elif password != confirmation:
            return render_template("signup.html", message5="*passwords don't match", name=name, surname=surname, username=username)
        db.execute("INSERT INTO users (name, surname, username, hash) VALUES(?, ?, ?, ?)", name, surname, username,
                   generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]
        return render_template("index1.html")
    else:
        return render_template("register.html")


@app.route("/tohome", methods=["GET", "POST"])
def tohome():
    if request.method == "POST":
        return render_template("index1.html")
    else:
        return render_template("index1.html")   

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        """Log user out"""

        # Forget any user_id
        session.clear()

        # Redirect user to login form
        return redirect("/")
    else:
        """Log user out"""

        # Forget any user_id
        session.clear()

        # Redirect user to login form
        return redirect("/")

@app.route("/staff", methods=["GET", "POST"])
def staff():
    if request.method == "POST":
        return render_template("staff.html")
    else:
        return render_template("staff.html")

@app.route("/tostaff", methods=["GET", "POST"])
def tostaff():
    if request.method == "POST":
        return render_template("logstaff.html")
    else:
        return render_template("logstaff.html")

@app.route("/courses", methods=["GET", "POST"])
def courses():
    if request.method == "POST":
        return render_template("courses.html")
    else:
        return render_template("courses.html")

@app.route("/tocourses", methods=["GET", "POST"])
def tocourses():
    if request.method == "POST":
        return render_template("logcourses.html")
    else:
        return render_template("logcourses.html")

@app.route("/feedbacks", methods=["GET", "POST"])
def feedbacks():
    if request.method == "POST":
        return render_template("feedbacks.html")
    else:
        return render_template("feedbacks.html")

@app.route("/tofeedback", methods=["GET", "POST"])
def tofeedback():
    if request.method == "POST":
        return render_template("logfeedbacks.html")
    else:
        return render_template("logfeedbacks.html")

@app.route("/faq", methods=["GET", "POST"])
def faq():
    if request.method == "POST":
        return render_template("faq.html")
    else:
        return render_template("faq.html")
@app.route("/tofaq", methods=["GET", "POST"])
def tofaq():
    if request.method == "POST":
        return render_template("logfaq.html")
    else:
        return render_template("logfaq.html")

@app.route("/six", methods=["GET", "POST"])
def six():
    if request.method == "POST":
        return render_template("logcourses.html")
    else:
        return render_template("logcourses.html")

@app.route("/seven", methods=["GET", "POST"])
def seven():
    if request.method == "POST":
        return render_template("course7.html")
    else:
        return render_template("course7.html")

@app.route("/eight", methods=["GET", "POST"])
def eight():
    if request.method == "POST":
        return render_template("course8.html")
    else:
        return render_template("course8.html")

@app.route("/nine", methods=["GET", "POST"])
def nine():
    if request.method == "POST":
        return render_template("course9.html")
    else:
        return render_template("course9.html")

@app.route("/ten", methods=["GET", "POST"])
def ten():
    if request.method == "POST":
        return render_template("course10.html")
    else:
        return render_template("course10.html")

@app.route("/eleven", methods=["GET", "POST"])
def eleven():
    if request.method == "POST":
        return render_template("course11.html")
    else:
        return render_template("course11.html")