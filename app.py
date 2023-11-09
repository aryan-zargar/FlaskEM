import commands.commands as FlaskEm
from flask import Flask
app = Flask(__name__)
db = FlaskEm.ConfigDataBase(app,"sqlite:///YOUR_DATABASE_NAME.db")