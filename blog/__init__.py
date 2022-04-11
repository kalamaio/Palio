# importa libreria flask
from flask import Flask
# Importa sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa migrate
from flask_migrate import Migrate
#importa configurazioni
from config import Config
# Importa login manager
from flask_login import LoginManager
from flask_admin import Admin






# Avvia istanza di flask sqlalchemy migrate e Config
app = Flask (__name__)
app.config.from_object (Config)
db = SQLAlchemy ( app )
migrate = Migrate ( app, db)
login_manager = LoginManager (app)
admin = Admin(app, template_mode='bootstrap3')


# Impostazione che serve solo con sqllight per limitazione del database
with app.app_context ():
    if db.engine.url.drivername == 'sqlite': #da verificare non funziona
        migrate.init_app (app, db, render_as_batch = True)
        
    else:
        migrate.init_app ( app, db )
        


# Importa file routes 
from blog import models, routes