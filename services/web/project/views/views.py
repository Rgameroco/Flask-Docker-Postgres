import os
from flask.views import MethodView
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
from ..models.jokes import Jokes
from utils.utils import replace_unicode_character
import json
from json import JSONEncoder
import logging

HEADERS = {'Content-type':'application/json','Accept':'text/plain'}

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class get_joke_chuck_or_dad(MethodView):
    def get(self,value):
        if(value == "Chuck"):
            response = requests.get(url="https://api.chucknorris.io/jokes/random")
        
        elif(value == "Dad"):
            response = requests.get(url="https://icanhazdadjoke.com/", headers=HEADERS)
            #response = replace_unicode_character(response.text)
            return jsonify(result=response.text)
        
        else:
            return "Invalid Parameter",400
    
        return jsonify(result=response.json())
    def post(self,value):
        try:
            jokes = Jokes(joke=value)
            jokes.save()
            return "Create a new imput", 200
        except:
            return "Error try again", 400
    
    def patch(self,id , joke):
        try:
            jokes = Jokes.query.get(id=id)
            jokes.joke = joke
            jokes.save()
            return f"Update {id} with {joke}", 200
        except:
            return "Error try again", 400
    
    def delete(self,id):
        try:
            jokes = Jokes.query.get(id=id)
            jokes.delete()
            return f"Delete {id}", 200
        except:
            return "Error try again", 400