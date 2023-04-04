from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
SQLALCHEMY_DATABASE_URI = 'sqlite:///pro.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
