from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
