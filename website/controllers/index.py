from flask import Flask, render_template, request, Blueprint

indexBlueprint = Blueprint('index', __name__)

@indexBlueprint.route('/index')
def index():
    return render_template("index.html")