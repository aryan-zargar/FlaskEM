from flask import Flask,render_template
from flask_sqlalchemy import *
def addPageHtml(FileName,**kwargs):
    theReturnDict = {}
    for key,value in kwargs.items():
        theReturnDict[key] = value
    return render_template(FileName,values=theReturnDict)
def addPage(data):
    return (data)
def ConfigDataBase(app,location):
    app.config['SQLALCHEMY_DATABASE_URI'] = location
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db
def SQLITE_DB_Add(db,value):
    db.session.add(value)
    db.session.commit()
def SQLITE_DB_Remove(db,objectClass,id):
    findedOBJ = objectClass.query.get_or_404(id)
    db.session.delete(findedOBJ)
    db.session.commit()
def SQLITE_DB_GetAll(objectClass):
    return objectClass.query.all()
