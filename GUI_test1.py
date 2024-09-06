# Imports
from tkinter import *
from tkinter import ttk
from datetime import date

# Root Window
root = Tk()
root.title("SPACECRAFT CENTRAL COMPUTER")
root.geometry("575x350")
root.config(bg="#000000")

tab_control = ttk.Notebook(root)

# Variables
command_var = StringVar()

# Tab Class
class CreateLayout:
    def __init__(self, window):
        self.window = window
        self.notebook = tab_control

        frame = Frame(root)
        frame.pack(fill=X)

        # Adding Classes to Tab Control
        self.notebook.add(TerminalTab(root), text="Terminal")
        self.notebook.add(MinigameTab(root), text="Minigame")
        self.notebook.pack(expand=1, fill="both")


# Terminal Tab Class
class TerminalTab(Frame):
    def __init__(self, master):
        super().__init__(master)
        pass


# Minigame Tab Class
class MinigameTab(Frame):
    def __init__(self, master):
        super().__init__(master)
        pass

terminal_tab = TerminalTab(tab_control)
minigame_tab = MinigameTab(tab_control)
tab_control.add(terminal_tab, text="Terminal")
tab_control.add(minigame_tab, text="Minigame")
tab_control.pack(expand=1, fill="both")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
tab_control.grid(column=0, row=0, sticky=E+W+N+S)

# Customization
terminal_tab.config(bg="#000000")

# Greeting Setup
weekday_greet = ""
today = date.today()

if today.weekday() == 0:
    weekday_greet = "Monday"
elif today.weekday() == 1:
    weekday_greet = "Tuesday"
elif today.weekday() == 2:
    weekday_greet = "Wednesday"
elif today.weekday() == 3:
    weekday_greet = "Thursday"
elif today.weekday() == 4:
    weekday_greet = "Friday"
elif today.weekday() == 5:
    weekday_greet = "Saturday"
else:
    weekday_greet = "Sunday"

# Screen Text
screentext = ["Welcome to the PERDITUS-26 OS\n"
            "Onboard systems courtesy of Sensus Corporation\n"
            "WARNING: ONBOARD TIME RELATIVITY SYSTEMS OFFLINE\n"
            "\n"
            "Happy " + weekday_greet + ".\n"
            "\n"
            'Type "Help" for a list of commands.'
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
            "There was no action supplied with that command."]

# Terminal Tab Screens
command_screen = Label(terminal_tab, text=screentext[0], font=("Courier", 12), fg="#00FF00", bg="#000000", anchor=W, justify="left")
entry = Entry(terminal_tab, textvariable=command_var, font=('Courier', 12), fg="#00FF00", bg="#000000")


# Commands
def run():
    command = command_var.get()
    if command == "Help":
        help()
    else:
        command_screen.config(text=screentext[2])
    entry.delete(0, 'end')
    command_var.set("")

def help():
    command_screen.config(text=screentext[1])

# Grid Packing
def pack():
    command_screen.pack(fill="both")
    entry.pack(fill="both", side=BOTTOM)

# Bind Keys
entry.bind("<Return>", (lambda event: run()))

# Mainloop
pack()
root.mainloop()