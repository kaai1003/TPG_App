#!/usr/bin/python3
""" TestModule class Module """
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class TestModule(BaseModel, Base):
    """TestModule class Definition

    Args:
        BaseModel (Class): base model class
        Base (Class): SqlAlchemy declarative Base
    """
    __tablename__ = 'testmodules'
    serial_number = Column("serial_number", String(128), nullable=False)
    terminals = Column("terminals", Integer, nullable=False)
    pushback = Column("pushback", Boolean, nullable=False)
    photo = Column("photo", String(128), nullable=True)
    supplier_id = Column("supplier_id", String(128),
                      ForeignKey("suppliers.id"), nullable=False)
    connector_id = Column("connector_id", String(128),
                      ForeignKey("connectors.id"), nullable=False)
    probeid = Column("probeid", String(128),
                      ForeignKey("testprobes.id"), nullable=False)
