#!/usr/bin/python3
"""This module outline the user class"""
import uuid

class User(AfyaModel):
    """Inherits from the AfyaModel"""
    email =""
    password =""
    first_name = ""
    last_name = ""


    def __init__(self, *args, **kwargs):
        """create instance of a user"""
        super().__init__(*args, **kwargs)

