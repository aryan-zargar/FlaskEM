from flask import Flask,render_template
from flask_sqlalchemy import *
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
def Create_DB(db):
    from app import db
    db.create_all()

    