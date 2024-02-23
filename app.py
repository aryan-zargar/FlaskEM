import commands.commands as FlaskEm
from flask import Flask
app = Flask(__name__)
db = FlaskEm.ConfigDataBase(app,"sqlite:///YOUR_DATABASE_NAME.db")

@app.route("/")
def mainpage():
    return FlaskEm.addPage("main.html",a="test value")