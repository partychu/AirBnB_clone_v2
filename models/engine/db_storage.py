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

#   def all(self, cls=None):

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
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()
