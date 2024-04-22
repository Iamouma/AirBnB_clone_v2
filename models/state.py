#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_relation = relationship("City", backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """This returns the citiy instances"""
        from models import storage
        matching_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                matching_cities.append(city)
        return matching_cities
