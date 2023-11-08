import commands.commands as FlaskEm
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main() :
    return FlaskEm.addPage("main.html",a = 5,b=7)