import os

from flask import Flask
from flask import render_template, request
from werkzeug.utils import redirect

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return render_template("index.html", title="Home")

    @app.route('/about')
    def about():
        return render_template("about.html", title="About")

    @app.route('/predict')
    def predict():
        return render_template("predict.html", title="Predict data")

    @app.route('/tech')
    def tech():
        return render_template("tech.html", title="Tech Stack")

    return app
