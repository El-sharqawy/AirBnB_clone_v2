#!/usr/bin/python3
"""This module defines a class to Database storage operations for
the HBnB clone project.
"""

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
from models.base_model import Base
from hashlib import md5
import os

MyClasses = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class DBStorage:
    """This class manages DB storage for the HBnB clone project."""

    __engine = None
    __session = None

    def __init__(self):
        """This method initializes an instance of the
        DBStorage class.
        """
        sr = os.getenv("HBNB_MYSQL_USER")
        sp = os.getenv("HBNB_MYSQL_PWD")
        sh = os.getenv("HBNB_MYSQL_HOST")
        sd = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(sr, sp, sh, sd),
            pool_pre_ping=True,
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method returns a dictionary of all instances
        of the class `cls` given as argument and returns
        all instances of all classes in db if given None.
        Args:
            cls(Class Obj): Class that the returned dictionary
                will contain instances of.
        """
        myDict = {}
        for Class in MyClasses:
            if cls is None or cls is MyClasses[Class] or cls is Class:
                results = self.__session.query(MyClasses[Class]).all()
                for obj in results:
                    key = obj.__class__.__name__ + "." + obj.id
                    myDict[key] = obj
        return myDict

        rDict = {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in myObjects}
        return rDict

    def new(self, obj):
        """Adds the object in the `obj` variable to the current
        database session.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database & creates the current
        database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """removes the current session"""
        self.__session.remove()
