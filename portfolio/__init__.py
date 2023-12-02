""""Module that creates the Flask app for this project"""
from flask import Flask, render_template, abort


app=Flask(__name__)


projects = [
    {
        "name": "Couple Ways - Trip Planner with Python and MongoDB",
        "thumb": "img/couple_ways_thumb.jpg",
        "hero": "img/couple_ways-hero.jpg",
        "categories": ["python", "flask", "web"],
        "slug": "couple-ways",
        "prod": "https://couple-ways.onrender.com",
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