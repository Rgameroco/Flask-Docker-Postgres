import os

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    make_response,
    redirect,
    url_for,
    request
)
import requests
from flask_sqlalchemy import SQLAlchemy
import json
from json import JSONEncoder
import logging
from .views.views import *
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
db.init_app(app)
Migrate(app,db)
jokes = get_joke_chuck_or_dad.as_view('get_joke_chuck_or_dad_api')
app.add_url_rule('/jokes$value=<value>',view_func=jokes, methods = ['GET'])
app.add_url_rule('/jokes$value=<value>',view_func=jokes, methods = ['POST'])
app.add_url_rule('/jokes$id=<id>$joke=<joke>',view_func=jokes, methods = ['PATCH'])
app.add_url_rule('/jokes$id=<id>',view_func=jokes, methods = ['DELETE'])