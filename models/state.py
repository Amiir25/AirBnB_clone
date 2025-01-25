#!/usr/bin/python3

"""
state.py

This module provides a `State` class whcich inherits the
'BaseModel' class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines a class that inherits the `BaseModel` class

    Attribute:
        name (string) - Name of the State
    """

    name = ""
