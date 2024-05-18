#!/usr/bin/python3
"""State Module for HBNB project"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":

        @property
        def cities(self):
            citieslist = []
            my_cities = models.storage.all(City)
            for city in my_cities.values():
                if city.state_id == self.id:
                    citieslist.append(city)
            return citieslist
