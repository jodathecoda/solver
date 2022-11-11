#copyright (c) 2019
#jodathecoda@yahoo.com

import sys, os
import time
import sqlite3
import settings
import pokerface

class Rank:
    def __init__(self):
        self.name = " "
        self.value = 0
        self.aggression = 0
        self.sea = "blue sea"
        if not settings.list_faces:
            p = pokerface.Pokerface()
            settings.list_faces = p.faces
        self.face = settings.list_faces.pop()