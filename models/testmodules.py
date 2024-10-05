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
    __table__ = 'testmodules'
    serial_number = Column("serial_number", String(128), nullable=False)
    terminals = Column("terminals", Integer, nullable=False)
    pushback = Column("pushback", Boolean, nullable=False)
    photo = Column("photo", String(128), nullable=True)
    supplier_id = Column("supplier_id", String(128),
                      ForeignKey("suppliers.id"), nullable=False)
    connector_id = Column("connector_id", String(128),
                      ForeignKey("connectors.id"), nullable=False)
    probeid_1 = Column("probeid_1", String(128),
                      ForeignKey("testprobes.id"), nullable=False)
    probeid_2 = Column("probeid_2", String(128),
                      ForeignKey("testprobes.id"), nullable=False)
    probeid_3 = Column("probeid_3", String(128),
                      ForeignKey("testprobes.id"), nullable=False)
    probeid_4 = Column("probeid_4", String(128),
                      ForeignKey("testprobes.id"), nullable=False)
    probeid_5 = Column("probeid_5", String(128),
                      ForeignKey("testprobes.id"), nullable=False)
    user_id = Column("user_id", String(128),
                      ForeignKey("users.id"), nullable=False)
