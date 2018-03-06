from flask_io import FlaskIO
from flask_sqlalchemy import SQLAlchemy
from dictalchemy import DictableModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(cls=DictableModel)
db = SQLAlchemy()
io = FlaskIO()
