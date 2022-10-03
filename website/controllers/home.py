from flask import Flask, Blueprint, render_template, request

homeBlueprint = Blueprint('home', __name__)

@homeBlueprint.route('/home')
def home():
    return render_template("home.html")