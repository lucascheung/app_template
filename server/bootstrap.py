import os
import sys

# Add base directory to path so that the api repo can depend on the open_api_core_3 repo.
_CUR_DIR = os.path.split(os.path.realpath(__file__))[0]
_BASE_DIR = os.path.join(_CUR_DIR, "../..")
sys.path.insert(0, _BASE_DIR)

import gunicorn
from flask import Flask
from flask_cors import CORS
from server.exts import db
from server.seed import seed
from server.clients import init_db
from server.urls import register_urlpatterns
from server.config.config import IS_DEV
from server.common.constants import *

def init_app():
    app = Flask(__name__, static_url_path=f'/')       # instantiate the app
    app.config.from_object(__name__)                         # setup Flask config
    app.config.from_pyfile('config/flask_config.py')          # setup Flask config--Local Configs
    # init_db(app)                                              # initiate database
    CORS(app, resources={r'/*': {'origins': '*'}})            # enable CORS
    # gunicorn.init_flask(app)                              # enable gunicorn
    register_urlpatterns(app)                                 # setup routes
    return app

app = init_app()

# Run w/ Local gunicorn:
# gunicorn server.bootstrap:app -b :5000 -w 1 --timeout 200
