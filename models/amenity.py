#!/usr/bin/python3
""" AirBnB clone - The console"""
from .base_model import BaseModel


class amenity(BaseModel):
    """Define the Amenity class"""
    name: str = ""