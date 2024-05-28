#!/usr/bin/python3

from  uuid import uuid4
from datetime import datetime
#import models

class AfyaModel:
    """Afya model for common attributes/methods"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.created_at


    def __str__(self):
        return "{}".format(self.__dict__)
