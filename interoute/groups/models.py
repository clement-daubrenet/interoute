from .. import db, Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from datetime import datetime


class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(UUID, primary_key=True)
    name = Column(String(30), nullable=False)
