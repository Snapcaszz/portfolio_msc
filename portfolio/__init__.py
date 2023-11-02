""""Module that creates the Flask app for this project"""
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    """Route for the portfolio home page"""
    return render_template("home.html")

@app.route("/about")
def about():
    """Route for the portfolio about page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Route for the portfolio contact page"""
    return render_template("contact.html")
