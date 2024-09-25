# resources.py
from tkinter import *

class Planet():
    def __init__(self, name, distance, resources, lore, code, destination):
        super().__init__()
        self.name = name
        self.distance = distance
        self.resources = resources
        self.lore = lore
        self.code = code
        self.destination = destination
