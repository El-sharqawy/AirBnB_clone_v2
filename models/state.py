#!/usr/bin/python3
"""State Module for HBNB project"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    if models.storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":

        @property
        def cities(self):
            from models import storage

            citieslist = []
            for key, value in storage.all().items():
                if type(value).__name__ == "City":
                    if (
                        "state_id" in value.__dict__
                        and str(value.__dict__["state_id"]) == self.id
                    ):
                        citieslist.append(value)
            return citieslist
