import os

from flask import Flask
from flask import render_template, request
from werkzeug.utils import redirect
import pandas as pd
import tensorflow
from tensorflow import keras
from keras.models import load_model

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

    global graph
    graph = tf.get_default_graph()
    model = load_model('model.h5')
        
    @app.route('/')
    def home():
        return render_template("index.html", title="Home")

    @app.route('/about')
    def about():
        return render_template("about.html", title="About")

    @app.route('/predict', methods=["GET", "POST"])
    def predict():
        data = {"success": False}
        params = flask.request.json
        if (params == None):
            params = flask.request.args

        # if parameters are found, return a prediction
        if (params != None):
            x=pd.DataFrame.from_dict(params, orient='index').transpose()
            with graph.as_default():
                data["prediction"] = str(model.predict(x)[0][0])
                data["success"] = True
        # return a response in json format 
        return flask.jsonify(data)
        return render_template("predict.html", title="Predict data")

    @app.route('/tech')
    def tech():
        return render_template("tech.html", title="Tech Stack")

    return app
