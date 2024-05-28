#!/usr/bin/python3
import h3

class Chemist(AfyaModel):
    """Chemist class mapped on the geographical """

    location = ""
    latitude = ""
    longitude = ""
    address = ""

    def __init__(self, *args, *kwargs):
        super().__init__(*args, **kwargs)
