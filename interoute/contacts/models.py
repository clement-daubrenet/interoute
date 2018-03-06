from .. import db, Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, ForeignKey, String, text


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = Column(UUID, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(125), nullable=False)
    phone = Column(String(30), nullable=False)
    group_id = Column(ForeignKey('groups.id', ondelete='CASCADE'))

    group = relationship('Group', lazy='noload')


"""CREATE TABLE contacts (
 id uuid PRIMARY KEY,
 first_name VARYING CHARACTER(30) NOT NULL,
 last_name VARYING CHARACTER(30) NOT NULL,
 email text NOT NULL UNIQUE,
 phone text NOT NULL UNIQUE,
 created timestamp DEFAULT now(),
group_id uuid, FOREIGN KEY(group_id) REFERENCES groups(group_id));"""


"""CREATE TABLE groups (
 id uuid PRIMARY KEY,
 name VARYING CHARACTER(30) NOT NULL,
 created datetime);"""