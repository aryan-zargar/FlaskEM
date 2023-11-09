import commands.commands as FlaskEm
app = FlaskEm.create_app()
db = FlaskEm.ConfigDataBase(app,"sqlite:///YOUR_DATABASE_NAME.db")