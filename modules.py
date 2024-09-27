# resources.py
from tkinter import *

class Module():
    def __init__(self, name, durability, data, online):
        super().__init__()
        self.name = name
        self.durability = durability
        self.data = data
        self.online = online

# Modules
maininteg = Module(name="Main Integrity: ", durability=100.0, data=1, online="ONLINE")
winginteg = Module(name="Wing Integrity: ", durability=100.0, data=1, online="ONLINE")
hullinteg = Module(name="Hull Integrity: ", durability=100.0, data=1, online="ONLINE")
shipinteg = int(maininteg.data + winginteg.data + hullinteg.data)
# Data Modules
nodes = Module(name="08 Status Nodes: ", durability=None, data=1, online="ONLINE")
radar = Module(name="Radar Reciever: ", durability=None, data=0, online="OFFLINE")
shields = Module(name="Shield Systems: ", durability=1000.0, data=0, online="OFFLINE")
modules = int(nodes.data + radar.data + shields.data)
