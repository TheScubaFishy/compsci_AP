# resources.py
from tkinter import *

class Planet():
    def __init__(self, name, distance, resources, lore, code):
        super().__init__()
        self.name = name
        self.distance = distance
        self.resources = resources
        self.lore = lore
        self.code = code

# Planets
space = Planet(name="Outer Space", distance="N/A", resources="Celestial Bodies, The Creature",
                lore=["You peer out your window. It feels bleak. It's all going dark."
                      ,
                      "---------------------------------------------------------\n"
                      "\n"],
                code="0")
dock = Planet(name="Interstellar Dock", distance=2, resources="None", 
                lore=["Property of Sensus Corporation. Outgoing broadcast: SOS... SOS..."
                      ,
                      "---------------------------------------------------------\n"
                      "\n"
                      "\n"
                      "[Interstellar Dock]: WELCOME TO INTERSTELLAR DOCK, SENSUS_CORP-0556\n"
                      "[Interstellar Dock]: FUEL RESERVE SCHEDULED FOR TOP-OFF\n"
                      "[Interstellar Dock]: POWER CELL CHARGING BAY: ACTIVE - 84H LEFT\n"
                      "\n"
                      "\n"
                      "Local Data Scan grants INTERSTELLAR DOCK a hazard level of SAFE.\n"
                      "WARNING: LOCAL LIFE FORMS UNUSUALLY LOW. MAINTAIN CAUTION.\n"
                      "\n"
                      "Nearby Tech: D4_BEACON, DOCKING_ARM-03, FUEL_HOSE-07, D4_STATUS_NODES\n"
                      "\n"
                      "\n"
                      "INFO: New data uploaded to Planetary Positioning System\n"],
                code="D4")
ilvadus = Planet(name="Ilvadus", distance=2.5, resources="Metal Scrap, Unrefined Texogrium",
                lore=["Located in the Viocichi Belt. This planet unlikely to harbor life."],
                code="I8")
teliv = Planet(name="Teliv", distance=3, resources="Ogurn Robotics Laboratory, Metal Scrap",
                lore=["Ogurn Robotics Lab has been inoperational after the PONOV-U5 disaster."],
                code="T3")
utreon = Planet(name="Utreon", distance=3.5, resources="Ion Glass Deposits, Acid Pools, Niobium Crystals",
                lore=["Proximity to host star led to spreading of Metallophagous Bacterium."],
                code="U2")
vizuno = Planet(name="Vizuno", distance=5, resources="Pahiri Foreign Biology Laboratory, Metal Scrap",
                lore=["Located at the edge of the Horn Nebula. Planet under quarantine."],
                code="V7")
orion = Planet(name="Orion", distance=7, resources="No Data Available",
                lore=["No Data Available. (ERROR 17: MANUAL DATA WIPE)"],
                code="O5")
planet_list = [dock, ilvadus, teliv, utreon, vizuno, orion]
