import commands.commands as FlaskEm
from flask import Flask
app = Flask(__name__)
db = FlaskEm.ConfigDataBase(app,"sqlite:///test.db")
# @app.route("/")
# def function():
#   FlaskEm.AddPage("main.html",a=5,b=7)

# @app.route("/test")
# def function():
#   FlaskEm.AddPage("test.html",abbas='484',b=7)
