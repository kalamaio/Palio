import os
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath ( os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get ('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join ( basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False