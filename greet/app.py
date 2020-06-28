from flask import Flask
app = Flask(__name__)


@app.route("/welcome")
def welcome_page():
    return f"Welcome"


@app.route("/welcome/home")
def welcome_home():
    return f"welcome home"


@app.route("/welcome/back")
def welcome_back():
    return f"Welcome back"
