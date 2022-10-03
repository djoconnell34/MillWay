from flask import Flask, Blueprint, request, render_template

def create_app():
    app = Flask(__name__)

    from .controllers.home import homeBlueprint
    app.register_blueprint(homeBlueprint, url_prefix='/')

    from .controllers.index import indexBlueprint
    app.register_blueprint(indexBlueprint, url_prefix='/')

    return app