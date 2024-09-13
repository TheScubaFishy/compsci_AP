# root.py
from tkinter import *
from tkinter import ttk
from terminal_tab import TerminalTab
from radar_tab import RadarTab

class Root(Tk):
   def __init__(self):
        super().__init__()
        # Customization
        self.title("SPACECRAFT CENTRAL COMPUTER")
        self.geometry("575x350")
        self.config(bg="#000000")

        # Tab Control
        self.notebook = ttk.Notebook(self)

        frame = Frame(self)
        frame.pack(fill=X)

        # Adding Classes to Tab Control
        self.notebook.add(TerminalTab(self), text="Terminal")
        self.notebook.add(RadarTab(self), text="Radar")
        self.notebook.pack(expand=1, fill="both")

