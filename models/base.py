#!/usr/bin/python3
"""Base Module"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel():
    """base class model definition"""
    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column("created_at",
                        DateTime(timezone=True),
                        nullable=False,
                        default=datetime.now())
    updated_at = Column("updated_at",
                        DateTime(timezone=True),
                        nullable=False,
                        default=datetime.now())

    def __init__(self, *args, **kwargs):
        """BaseModel Initialisation Method"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """object instance string repr"""
        dict = self.__dict__.copy()
        dict.pop("_sa_instance_state", None)
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, dict)

    def to_dict(self):
        """convert object instance to dict"""
        inst_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                inst_dict[key] = datetime.isoformat(value)
            elif key != '_sa_instance_state':
                inst_dict[key] = value
        inst_dict['__class__'] = self.__class__.__name__
        return inst_dict
