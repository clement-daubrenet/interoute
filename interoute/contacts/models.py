from .. import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = Column(UUID, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(125), nullable=False)
    phone = Column(String(30), nullable=False)
    group_id = Column(ForeignKey('groups.id', ondelete='CASCADE'))

    group = relationship('Group', lazy='noload')
