# this file makes sure to initialise our taskmanager application as a apackage allowing us to use our own imports as well as any standard imports 


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"): # only import env if the os can find an existing file path for the env.py file itself
    import env  # noqa


app = Flask(__name__) # can create an instance of the imported Flask() class, and that will be stored in a variable called 'app', which takes the default Flask __name__ module
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app) # create an instance of the imported SQLAlchemy class which will be assigned to a var db and set to the instance of our flask app

from taskmanager import routes  # noqa

