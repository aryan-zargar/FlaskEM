from flask import Flask,render_template
from flask_sqlalchemy import *
def create_app():
    return Flask(__name__)
def addPage(FileName,**kwargs):
    theReturnDict = {}
    for key,value in kwargs.items():
        theReturnDict[key] = value
    return render_template(FileName,values=theReturnDict)
def ConfigDataBase(app,location):
    app.config['SQLALCHEMY_DATABASE_URI'] = location
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db
def Create_DB():
    from app import db
    db.create_all()
def Create_DB_Class(**kwargs):
    from app import db
    class Create_CLass(db.Model):
        id = db.Column(db.Integer , primary_key = True)
        for key,Type in kwargs.items():
            if Type.lower() == "string":
                key = db.Column(db.String(500))
            if Type.lower() == "integer":
                key = db.Column(db.integer)
            if Type.lower() == "blob":
                key = db.Column(db.BLOB)
    return Create_CLass