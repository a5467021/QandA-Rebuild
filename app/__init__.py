'''
Backend of Program Q And A.

Author: a5467021
2018/4/20
'''

import time
from flask import Flask, Blueprint
from flask_cors import CORS
from configs.config import config
from app.extra import db
from app.resource import RandomQuestion
from flask_restful import Api


app_blueprint = Blueprint('QAndA', __name__)
app_api = Api(app_blueprint)
app_api.add_resource(RandomQuestion, '/rand_question')

def register(app):
    app.register_blueprint(app_blueprint, url_prefix='/api/v2')

def create_app(config_name):
    '''create app'''
    app = Flask(__name__)
    app.config.from_object(config[config_name]())
    db.init_app(app)
    register(app)
    CORS(app)

    return app, db