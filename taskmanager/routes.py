from flask import render_template # start using flask functionality
from taskmanager import app, db # from taskmanager package import app and db

# for simpicity to get the app running, we will create a basic app route using the root level directory of / 
# this will be used to target a function called home which will just return the render template of base.html
@app.route("/")
def home():
    return render_template("base.html")