#!/usr/bin/python3
"""
State class from the models module
"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
STORAGE = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """State class manages all application states"""
    if STORAGE == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ''

        @property
        def cities(self):
            """
                Property method to return a list of City objects 
                associated with the current State
            """
            city_objects = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_objects.append(city)
            return city_objects
