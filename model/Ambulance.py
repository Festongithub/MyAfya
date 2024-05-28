#!/usr/bin/python3
import h3
from uuid import uuid4
class Ambulance:
    def __init__(self, ambulance_id, latitude, longitude ):
        self.ambulance_id = str(uuid4())
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.h3_index = h3.geo_to_h3(latitude, longitue, resolution=9)
        self.is_busy = False

    def update_location(self, new_longitude, new_latitude):
        """Update location of the ambulance"""
        self.longitude = longitude
        self.latitude = latitude
        self.h3_index = h3.geo_to_h3(latitude, longitue, resolution=9)

    def mark_busy(self):
        """Gets status of the ambulance schedule"""
        self.is_busy = True

    def mark_free(self):
        """Mark Ambulance as free"""
        self.is_busy = False

    def __str__(self):
        return f"Ambulance {self.ambulance_id} at ({self.latitude}, {self.longitude}), {'Busy' if self.is_busy else 'Free'}

   
