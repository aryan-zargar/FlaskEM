from flask import Flask,render_template

def addPage(FileName,**kwargs):
    theReturnDict = {}
    for key,value in kwargs.items():
        theReturnDict[key] = value
    print(theReturnDict)
    return render_template(FileName,values=theReturnDict)
