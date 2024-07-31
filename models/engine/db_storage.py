#!/usr/bin/python3
"""
Database management engine
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """
    Manages long-term storage for class instances
    """
    CLASS_MAP = {
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }

    __engine = None
    __session = None


    def __init__(self):
        """
        Initializes the storage engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB')))
        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """
        Retrieves a dictionary of all objects of a given class, or all classes
        """
        objects = {}
        if cls is not None:
            query = self.__session.query(DBStorage.CLASS_MAP[cls])
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            return objects


        for class_type in DBStorage.CLASS_MAP.values():
            query = self.__session.query(class_type)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects


    def new(self, obj):
        """
        Adds an object to the current database session
        """
        self.__session.add(obj)


    def save(self):
        """
        Commits all changes to the current database session
        """
        self.__session.commit()


    def rollback_session(self):
        """
        Rolls back the current database session in case of an error
        """
        self.__session.rollback()


    def delete(self, obj=None):
        """
        Deletes an object from the current database session, if provided
        """
        if obj:
            self.__session.delete(obj)
            self.save()


    def delete_all(self):
        """
        Deletes all objects from the storage, used for testing purposes
        """
        for class_type in DBStorage.CLASS_MAP.values():
            query = self.__session.query(class_type)
            all_objects = [obj for obj in query]
            for _ in range(len(all_objects)):
                to_delete = all_objects.pop(0)
                to_delete.delete()
        self.save()


    def reload(self):
        """
        Creates all tables in the database and initializes a new session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))


    def close(self):
        """
        Closes the current session by calling remove() on the session attribute
        """
        self.__session.remove()


    def get(self, cls, id):
        """
        Retrieves a single object by class name and id
        """
        if cls and id:
            key = "{}.{}".format(cls, id)
            all_objects = self.all(cls)
            return all_objects.get(key)
        return None


    def count(self, cls=None):
        """
        Returns the total number of objects in storage
        """
        return len(self.all(cls))
