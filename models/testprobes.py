#!/usr/bin/python3
""" TestProbe class Module """
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class TestProbe(BaseModel, Base):
    """TestProbe class Definition

    Args:
        BaseModel (Class): base model class
        Base (Class): SqlAlchemy declarative Base
    """
    __table__ = 'testprobes'
    serial_number = Column("serial_number", String(128), nullable=False)
    stock_location = Column("stock_location", String(128), nullable=False)
    pushback = Column("pushback", Boolean, nullable=False)
    photo = Column("photo", String(128), nullable=True)
    datasheet = Column("datasheet", String(128), nullable=True)
    supplier_id = Column("supplier_id", String(128),
                      ForeignKey("suppliers.id"), nullable=False)
    user_id = Column("user_id", String(128),
                      ForeignKey("users.id"), nullable=False)
