#!/usr/bin/python3
""" User class Module """
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class Definition

    Args:
        BaseModel (Class): base model class
        Base (Class): SqlAlchemy declarative Base
    """
    __tablename__ = 'users'
    user = Column("user", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    role = Column("role", String(128), nullable=False)
