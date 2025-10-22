from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/discover")
def discover():
    return render_template("discover.html")

@app.route("/applicants")
def applicants():
    return render_template("applicants.html")

@app.route("/corporate")
def corporate():
    return render_template("corporate.html")

app.run(debug=True)