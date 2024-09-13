# terminal_tab.py
from tkinter import *
from datetime import date

class TerminalTab(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Customization
        self.config(bg="#000000")

        # Variables
        command_var = StringVar()

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
        
        # Escape Command
        def esc():
            self.command_screen.config(text=screentext[1])
            self.entry.delete(0, 'end')

        # Run Command
        def run():
            command = command_var.get()
            if command == "help" or command == "Help" or command == "HELP":
                help()
            elif command == "route" or command == "Route" or command == "ROUTE":
                route()
            else:
                self.command_screen.config(text=screentext[0])
            self.entry.delete(0, 'end')

        # HELP Command
        def help():
            self.command_screen.config(text=screentext[2])

        # ROUTE Command
        def route():
            self.command_screen.config(text=screentext[3])

        # Screen Text
        screentext = ["There was no action supplied with that command.\n"
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
                    "To route the ship to the desired planet, use the word ROUTE.\n"
                    "To learn more about a specific planet, use the word INFO.\n"
                    "---------------------------------------------------------\n"
                    "\n"
                    "* Interstellar Dock\n"
                    "\n"
                    "* Adion-15\n"
                    "* Axosie-66\n"
                    "* Hakarvis-22\n"
                    "\n"
                    "* Drypso-12\n"
                    "* Iliv-07\n"
                    "* Rogigawa-87\n"
                    "\n"
                    "* Itillon-48\n"
                    "* Hietomia-21\n"]

        # Terminal Tab Screens
        self.command_screen = Label(self, text=screentext[1], font=("Courier", 12), fg="#00FF00", bg="#000000", anchor=W, justify="left")
        self.command_screen.pack(fill="both")
        self.entry = Entry(self, textvariable=command_var, font=('Courier', 12), fg="#00FF00", bg="#000000")
        self.entry.pack(fill="both", side=BOTTOM)

        # Bind Keys
        self.entry.bind("<Return>", (lambda event: run()))
        self.entry.bind("<Escape>", (lambda event: esc()))

