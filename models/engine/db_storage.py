#!/usr/bin/python3
"""Mysql Database Module"""
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base import BaseModel, Base
from models.connectors import Connector
from models.suppliers import Supplier
from models.testmodules import TestModule
from models.testprobes import TestProbe
from models.users import User

classes = {'Connector': Connector,
           'Supplier': Supplier,
           'TestModule': TestModule,
           'TestProbe': TestProbe,
           'User': User}

class DBStorage:
    """Mysql DBStorage class definition"""
    def __init__(self):
            """engine DB initialisation"""
            user = 'tpg_dev'
            pwd = quote('tpg@12_34')
            host = 'localhost'
            db = 'tpg_dev_db'
            self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                        format(user,
                                                pwd,
                                                host,
                                                db), pool_pre_ping=True)

    def reload(self):
        """create all tables on DB"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """load objects from DB
        Args
            cls (class): class name to be loaded
        """
        objs_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
            """add obj to DB
            Args
                obj: object to add
            """
            self.__session.add(obj)

    def save(self):
        """commit changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from DB
        Args
            obj: object to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """method to retrieve one object
        Args
            cls(object): class object
            id(object attribute): string rep of instance object
        """
        objects = self.all(cls)
        for obj in objects.values():
            if obj.id == id:
                return (obj)
        return None

    def close(self):
        """call remove or cloase session"""
        self.__session.remove()
