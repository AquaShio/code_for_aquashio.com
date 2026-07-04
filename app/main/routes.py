from flask import render_template
from app.main import main

@main.route("/")
def index():
    return render_template("main/home.html")

@main.route("/projects")
def projects():
    return render_template("main/projects.html")

@main.route("/about")
def about():
    return render_template("main/about.html")