# resources.py
from tkinter import *

class Module():
    def __init__(self, name, durability, data, online):
        super().__init__()
        self.name = name
        self.durability = durability
        self.data = data
        self.online = online
