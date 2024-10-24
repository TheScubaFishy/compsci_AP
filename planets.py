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
                lore=["Located in the Viocichi Belt. This planet unlikely to harbor life.",
                      "---------------------------------------------------------\n"
                      "\n"
                      "\n"
                      "[Unknown]: .. .-.. ...- .- -.. ..- ...\n"
                      "[Unknown]: .... --- ... - .. .-.. .\n"
                      "[Unknown]: .-.. . .- ...- . / -. --- .--\n"
                      "\n"
                      "\n"
                      "Local Data Scan grants ILVADUS a hazard level of C+.\n"
                      "WARNING: LIFE FORMS APPROACHING SHIP\n"
                      "\n"
                      "Nearby Tech: I8_BEACON\n"
                      "\n"
                      "\n"
                      "INFO: New data uploaded to Planetary Positioning System\n"],
                code="I8")
teliv = Planet(name="Teliv", distance=3, resources="Ogurn Robotics Laboratory, Metal Scrap",
                lore=["Ogurn Robotics Lab has been inoperational after the PONOV-U5 disaster.",
                      "---------------------------------------------------------\n"
                      "\n"
                      "\n"
                      "[Ogurn Lab]: W#LC#ME T# OG#RN R#B#TICS LAB#R#TOR#\n"
                      "[Ogurn Lab]: R#D##TION L#VEl#: H#GH\n"
                      "[Ogurn Lab]: P#EA#E EXC#RC##E CA##ION\n"
                      "\n"
                      "\n"
                      "Local Data Scan grants TELIV a hazard level of B.\n"
                      "WARNING: HIGH LOCAL RADIATION LEVELS\n"
                      "\n"
                      "Nearby Tech: T3_BEACON, OGURN_DOCKER_1, OGURN_DOCKER_3, PONOV-U5\n"
                      "\n"
                      "\n"
                      "INFO: New data uploaded to Planetary Positioning System\n"],
                code="T3")
utreon = Planet(name="Utreon", distance=3.5, resources="Ion Glass Deposits, Acid Pools, Niobium Crystals",
                lore=["Proximity to host star led to spreading of Metallophagous Bacterium.",
                      "---------------------------------------------------------\n"
                      "\n"
                      "\n"
                      "Welcome to planet Utreon, Captain.\n"
                      "This planet is extremely hostile to life forms of your kind.\n"
                      "If possible, use commands to interact with deployable tech.\n"
                      "\n"
                      "\n"
                      "Local Data Scan grants UTREON a hazard level of A.\n"
                      "WARNINGS ARE NOT AVAILIBLE ON THIS PLANET\n"
                      "\n"
                      "Nearby Tech: U2_BEACON\n"
                      "\n"
                      "\n"
                      "INFO: New data uploaded to Planetary Positioning System\n"],
                code="U2")
vizuno = Planet(name="Vizuno", distance=5, resources="Pahiri Foreign Biology Laboratory, Metal Scrap",
                lore=["Located at the edge of the Horn Nebula. Planet under quarantine.",
                      "---------------------------------------------------------\n"
                      "\n"
                      "\n"
                      "[Pahiri Biolab]: WARNING: THIS PLANET (VIZUNO) IS UNDER QUARANTINE\n"
                      "[Pahiri Biolab]: WE AT PAHIRI BIOLAB CANNOT ALLOW YOUR SHIP TO LEAVE\n"
                      "* WARNING: BACK LEFT, FRONT RIGHT, AND MAIN THRUSTERS DAMAGED\n"
                      "[Pahiri Biolab]: PLEASE ENJOY YOUR STAY\n"
                      "\n"
                      "\n"
                      "Local Data Scan is damaged. Scan unavailible.\n"
                      "\n"
                      "Nearby Tech: V7_BEACON, UNKNOWN_1, UNKNOWN_2, UNKNOWN_3, UNKNOWN_4\n"
                      "\n"
                      "\n"
                      "INFO: New data uploaded to Planetary Positioning System\n"],
                code="V7")
orion = Planet(name="Orion", distance=7, resources="No Data Available",
                lore=["No Data Available. (ERROR 17: MANUAL DATA WIPE)",
                      "---------------------------------------------------------\n"
                      "\n"
                      "\n"
                      "[Sensus Corp.]: LEAVE THIS PLANET. YOU ARE A FOREIGN ENTITY.\n"
                      "[Sensus Corp.]: YOUR CONTRACT WITH US HAS BEEN TERMINATED.\n"
                      "[Sensus Corp.]: NEVER RETURN TO THIS PLANET, AND SPEAK NOT OF US.\n"
                      "\n"
                      "\n"
                      "Local Data Scan grants ORION a hazard level of S++.\n"
                      "WARNING: ALL TECH ON THIS SHIP HAS BEEN DISABLED\n"
                      "\n"
                      "Nearby Tech: O5_BEACON, O5_DYSON_SPHERE, SENSUS_SATTELITE_075, +19k more\n"
                      "\n"
                      "\n"
                      "INFO: O5 data wipe successful.\n"],
                code="O5")
planet_list = [dock, ilvadus, teliv, utreon, vizuno, orion]
