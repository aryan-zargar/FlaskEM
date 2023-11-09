import commands.commands as FlaskEm
app = FlaskEm.create_app()
db = FlaskEm.ConfigDataBase(app,"sqlite:///YOUR_DATABASE_NAME.db")
my_class = FlaskEm.Create_DB_Class(username = "string",password="string")
print(my_class(username = "abbas",password="mohammad"))