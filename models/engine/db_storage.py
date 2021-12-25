#!/usr/bin/python3
"""
New engine DBStorage
"""

from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """SQLAlchemy engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Engine constructor"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns query on current database"""

        newdict = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                newdict[cls + "." + obj.id] = obj
        else:
            for key, value in self.hbnb_classes.items():
                try:
                    query = self.__session.query(value).all()
                except:
                    pass
                for obj in query:
                    newdict[key + "." + obj.id] = obj

        return newdict




        """a_d = {}

        if cls is None:
            for c in classes:
                obj = self.__session.query(classes[c]).all()
                for o in obj:
                    a_d[o.__class__.__name__ + '.' + o.id] = o
        else:
            obj = self.__session.query(cls)
            for o in obj:
                a_d[o.__class__.__name__ + '.' + o.id] = o
        return a_d"""

    def new(self, obj):
        """Add object"""
        self.__session.add(obj)

    def save(self):
        """Commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
