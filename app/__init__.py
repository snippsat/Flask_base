from flask import Flask, Blueprint
from .extensions import db
from .views import my_app
import os

def create_app(config_file='extensions.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")  
    app.register_blueprint(my_app)
    db.init_app(app)
    return app

def create_db(app):
    with app.app_context():
        db.create_all()
    print('Created Database!')

#-- When database is created can comment out this line
#-- If forget will not overwrite tables if they are already in the database
create_db(create_app())
