from .. import db, Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, ForeignKey, String, text


class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(UUID, primary_key=True)
    name = Column(String(30), nullable=False)
