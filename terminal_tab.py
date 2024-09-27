# terminal_tab.py
from tkinter import *
from datetime import date
from planets import planet_list, space, dock, ilvadus, teliv, utreon, vizuno, orion
from modules import shipinteg, maininteg, winginteg, hullinteg, modules, nodes, radar, shields
from resources import credits, fuel, power, food
from shipdata import ShipData


class TerminalTab(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Customization
        self.config(bg="#000000")

        # Variables
        command_var = StringVar()

        # Ship Data
        ship = ShipData(status="Routing", weather="Normal", event="No Remarks", course_try=None, course_set=space, course_dist=0)

        # Greeting Setup
        def greeting():
            today = date.today()
            if today.weekday() == 0:
                return "Monday"
            elif today.weekday() == 1:
                return "Tuesday"
            elif today.weekday() == 2:
                return "Wednesday"
            elif today.weekday() == 3:
                return "Thursday"
            elif today.weekday() == 4:
                return "Friday"
            elif today.weekday() == 5:
                return "Saturday"
            else:
                return "Sunday"
        
        # Refresh Screens
        def refresh_planet():
            runtext[1] = ("Welcome to the PERDITUS-26 OS\n"
            "Onboard systems courtesy of Sensus Corporation\n"
            "WARNING: ONBOARD TIME RELATIVITY SYSTEMS OFFLINE\n"
            "\n"
            "Happy " + greeting() + ".\n"
            "\n"
            "Ship is " + str(ship.course_dist) + " Light Years away from " + ship.course_set.name + "\n"
            "Current weather: " + ship.weather + "\n"
            "\n"
            "Remarks: " + ship.event + "\n"
            "\n"
            'Type "Help" for a list of commands.\n')
        
        def refresh_status():
            screentext[4] = "PERDITUS-26 sent scan request to 08 STATUS NODES.\n"
            "08 STATUS NODES require passphrase for access: ********\n"
            "Admin identity confirmed. Scan yielded following results:\n"
            "---------------------------------------------------------\n"
            "\n"
            "SHIP INTEGRITY: " + str(shipinteg) + " OF 3 ONLINE\n"  
            "* " + maininteg.name + str(maininteg.durability) + "%\n"
            "* " + winginteg.name + str(winginteg.durability) + "%\n"
            "* " + hullinteg.name + str(hullinteg.durability) + "%\n"
            "\n"
            "LIFE SUPPORT SYSTEMS: 1 OF 3 ONLINE\n"
            "* Captain Life Support: ONLINE\n"
            "* Crew 1 Life Support: OFFLINE\n"
            "* Crew 2 Life Support: OFFLINE\n"
            "\n"
            "EXTERIOR DATA MODULES: " + str(modules) + " OF 3 ONLINE\n"  
            "* " + nodes.name + nodes.online + "\n"
            "* " + radar.name + radar.online + "\n"
            "* " + shields.name + shields.online + "\n"

        def refresh_resources():
            screentext[5] = "PERDITUS-26 sent inventory request to STORAGE BAY.\n"
            "STORAGE BAY requires passphrase for access: ********\n"
            "Captain confirmed. STORAGE BAY yielded following results:\n"
            "---------------------------------------------------------\n"
            "\n"
            "PRIORITY RESOURCES:\n" 
            "* " + credits.name + str(credits.value) + "\n"
            "* " + fuel.name + str(fuel.value) + "%\n"
            "* " + power.name + str(power.value) + "%\n"
            "\n"
            "SURVIVAL RESOURCES:\n" 
            "* " + food.name + str(food.value) + " Day(s) of Rations\n"
            
        # Escape Command
        def esc():
            if ship.course_set == None or ship.course_set == space:
                self.command_screen.config(text=screentext[1])
            else:
                self.command_screen.config(text=runtext[1])
            self.entry.delete(0, 'end')

        # Run Command
        def run():
            command = command_var.get()
            if ship.course_try == None:
                if command == "help" or command == "Help" or command == "HELP":
                    help()
                elif command == "route" or command == "Route" or command == "ROUTE":
                    route()
                elif command == "status" or command == "Status" or command == "STATUS":
                    status()
                elif command == "storage" or command == "Storage" or command == "STORAGE":
                    storage()
                else:
                    self.command_screen.config(text=screentext[0]) # Catch errors and put out error message
                    code(command) # If it's planet code, run planet info
            else:
                if command == "y" or "Y" or "yes" or "Yes" or "YES":
                    ship.course_set = ship.course_try
                    ship.course_dist = ship.course_set.distance 
                    refresh_planet()
                    self.command_screen.config(text=runtext[1])
                elif command == "n" or "N" or "no" or "No" or "NO":
                    route()
                ship.course_try = None
            self.entry.delete(0, 'end')

        # HELP Command
        def help():
            self.command_screen.config(text=screentext[2])

        # ROUTE Commands
        def route():
            self.command_screen.config(text=screentext[3])

        # Select Planet
        def code(planetcode):
            for planet in planet_list:
                if planetcode == planet.code:
                    current_planet = planet
                    self.command_screen.config(text="Autopilot routed to " + current_planet.code + " - " + current_planet.name + "\n"
                                            "Fuel required: " + str((current_planet.distance * 100.0) * fuel.value2) + "% of fuel tank.\n"
                                            "Current fuel levels: " + str(fuel.value) + "% of fuel tank.\n"
                                            "WARNING: IF FUEL LEVELS ARE LOW, DO NOT ROUTE AUTOPILOT!!\n"
                                            "---------------------------------------------------------\n"
                                            "\n"
                                            "* Planet Name: " + current_planet.name + "\n"
                                            "* Planet Distance: " + str(current_planet.distance) + " Light Years\n"
                                            "* Local Resources: " + current_planet.resources + "\n"
                                            "\n"
                                            + current_planet.lore + "\n"
                                            "\n"
                                            "\n"
                                            "Route Autopilot to " + current_planet.name + "?\n")
                    ship.course_try = current_planet

        # STATUS Command
        def status():
            self.command_screen.config(text=screentext[4])
        
        # STORAGE Command
        def storage():
            self.command_screen.config(text=screentext[5])

        # Screen Text
        screentext = ["There was no action supplied with that command.\n"
                    "In case of error, planetary codes are CASE SENSITIVE.\n"
                    'Type "Help" for a list of commands.\n'
                    ,
                    "Welcome to the PERDITUS-26 OS\n"
                    "Onboard systems courtesy of Sensus Corporation\n"
                    "WARNING: ONBOARD TIME RELATIVITY SYSTEMS OFFLINE\n"
                    "\n"
                    "Happy " + greeting() + ".\n"
                    "\n"
                    'Type "Help" for a list of commands.\n'
                    ,
                    ">ROUTE\n"
                    "To change the course of the autopilot.\n"
                    "\n"
                    ">STATUS\n"
                    "To scan the ship for potential damage.\n"
                    "\n"
                    ">STORAGE\n"
                    "To manage remaining resources.\n"
                    ,
                    "Welcome to the Planetary Positioning System.\n"
                    "To route the ship to a planet, input its planetary code.\n"
                    "Planetary code is CASE SENSITIVE. Type a correct command.\n"
                    "---------------------------------------------------------\n"
                    "\n"
                    "* " + dock.code + " - " + dock.name + "\n"
                    "\n"
                    "* " + ilvadus.code + " - " + ilvadus.name + "\n"
                    "* " + teliv.code + " - " + teliv.name + "\n"
                    "* " + utreon.code + " - " + utreon.name + "\n"
                    "\n"
                    "* " + vizuno.code + " - " + vizuno.name + "\n"
                    "* " + orion.code + " - " + orion.name + "\n"
                    ,
                    "PERDITUS-26 sent scan request to 08 STATUS NODES.\n"
                    "08 STATUS NODES require passphrase for access: ********\n"
                    "Admin identity confirmed. Scan yielded following results:\n"
                    "---------------------------------------------------------\n"
                    "\n"
                    "SHIP INTEGRITY: " + str(shipinteg) + " OF 3 ONLINE\n"  
                    "* " + maininteg.name + str(maininteg.durability) + "%\n"
                    "* " + winginteg.name + str(winginteg.durability) + "%\n"
                    "* " + hullinteg.name + str(hullinteg.durability) + "%\n"
                    "\n"
                    "LIFE SUPPORT SYSTEMS: 1 OF 3 ONLINE\n"
                    "* Captain Life Support: ONLINE\n"
                    "* Crew 1 Life Support: OFFLINE\n"
                    "* Crew 2 Life Support: OFFLINE\n"
                    "\n"
                    "EXTERIOR DATA MODULES: " + str(modules) + " OF 3 ONLINE\n"  
                    "* " + nodes.name + nodes.online + "\n"
                    "* " + radar.name + radar.online + "\n"
                    "* " + shields.name + shields.online + "\n"
                    ,
                    "PERDITUS-26 sent inventory request to STORAGE BAY.\n"
                    "STORAGE BAY requires passphrase for access: ********\n"
                    "Captain confirmed. STORAGE BAY yielded following results:\n"
                    "---------------------------------------------------------\n"
                    "\n"
                    "PRIORITY RESOURCES:\n" 
                    "* " + credits.name + str(credits.value) + "\n"
                    "* " + fuel.name + str(fuel.value) + "%\n"
                    "* " + power.name + str(power.value) + "%\n"
                    "\n"
                    "SURVIVAL RESOURCES:\n" 
                    "* " + food.name + str(food.value) + " Day(s) of Rations\n"]
        
        # Run Text
        runtext = ["There was no action supplied with that command.\n"
                    "In case of error, planetary codes are CASE SENSITIVE.\n"
                    'Type "Help" for a list of commands.\n'
                    ,
                    "Welcome to the PERDITUS-26 OS\n"
                    "Onboard systems courtesy of Sensus Corporation\n"
                    "WARNING: ONBOARD TIME RELATIVITY SYSTEMS OFFLINE\n"
                    "\n"
                    "Happy " + greeting() + ".\n"
                    "\n"
                    "Ship is " + str(ship.course_dist) + " Light Years away from " + ship.course_set.name + "\n"
                    "Current weather: " + ship.weather + "\n"
                    "\n"
                    "Remarks: " + ship.event + "\n"
                    "\n"
                    'Type "Help" for a list of commands.\n']

        # Terminal Tab Screens
        self.command_screen = Label(self, text=screentext[1], font=("Courier", 12), fg="#00FF00", bg="#000000", anchor=W, justify="left")
        self.command_screen.pack(fill="both")
        self.entry = Entry(self, textvariable=command_var, font=('Courier', 12), fg="#00FF00", bg="#000000")
        self.entry.pack(fill="both", side=BOTTOM)

        # Bind Keys
        self.entry.bind("<Return>", (lambda event: run()))
        self.entry.bind("<Escape>", (lambda event: esc()))

