'''
to make a database you need to do in cmd : 

flask shell 
- 
from app import db
db.create_all()

# just like flask
'''
import commands.commands as FlaskEm
from flask import Flask
app = Flask(__name__)
db = FlaskEm.ConfigDataBase(app,"sqlite:///YOUR_DATABASE_NAME.db")
# @app.route("/")
# def function():
#   FlaskEm.AddPage("main.html",a=5,b=7)

