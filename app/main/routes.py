from app.main import main

@main.route("/")
def index():
    return "Portfolio home — coming soon"
@main.route("/projects")
def projects():
    return "Projects page — coming soon"

@main.route("/about")
def about():
    return "About page — coming soon"