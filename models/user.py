#!/usr/bin/python3
"""Module that contain the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class define User"""
    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
