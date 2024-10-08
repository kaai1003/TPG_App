#!/usr/bin/python3
""" Supplier class Module """
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class Supplier(BaseModel, Base):
    """Supplier class Definition

    Args:
        BaseModel (Class): base model class
        Base (Class): SqlAlchemy declarative Base
    """
    __tablename__ = 'suppliers'
    name = Column("name", String(128), nullable=False)
    type = Column("type", String(128), nullable=False)
    user_id = Column("user_id", String(128),
                      ForeignKey("users.id"), nullable=False)
