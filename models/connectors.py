#!/usr/bin/python3
""" Connector class Module """
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Connector(BaseModel, Base):
    """Connetor class Definition

    Args:
        BaseModel (Class): base model class
        Base (Class): SqlAlchemy declarative Base
    """
    __table__ = 'connectors'
    part_number = Column("serial_number", String(128), nullable=False)
    terminals = Column("terminals", Integer, nullable=False)
    photo = Column("photo", String(128), nullable=True)
    supplier_id = Column("supplier_id", String(128),
                      ForeignKey("suppliers.id"), nullable=False)
    user_id = Column("user_id", String(128),
                      ForeignKey("users.id"), nullable=False)
