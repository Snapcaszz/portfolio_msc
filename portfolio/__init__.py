""""Module that creates the Flask app for this project"""
from flask import Flask, render_template, abort

app=Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "#",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
        "prod": "#",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
        "prod": "#",
    },
]

slug_to_project = {project['slug']: project for project in projects}

@app.route("/")
def home():
    """Route for the portfolio home page"""
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    """Route for the portfolio about page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Route for the portfolio contact page"""
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    """Route for each of our projects page"""
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(_):
    """Route for the page not found error"""
    return render_template("404.html"), 404