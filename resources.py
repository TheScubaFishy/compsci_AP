# resources.py
from tkinter import *

class Resource():
    def __init__(self, name, value, value2):
        super().__init__()
        self.name = name
        self.value = value
        self.value2 = value2

# Resources
credits = Resource(name="Credits: ", value=60, value2=None)
fuel = Resource(name="Fuel: ", value=100.0, value2=0.25)
power = Resource(name="Power Cells: ", value=100.0, value2=100.0)
food = Resource(name="Food: ", value=5, value2=None)
