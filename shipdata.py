# shipdata.py
from tkinter import *
from planets import space

class ShipData():
    def __init__(self, status, weather, event, course_try, course_set, course_dist):
        super().__init__()
        self.status = status
        self.weather = weather
        self.event = event
        self.course_try = course_try
        self.course_set = course_set
        self.course_dist = course_dist
