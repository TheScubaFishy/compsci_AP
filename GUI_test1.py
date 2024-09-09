# Imports
from tkinter import *
from tkinter import ttk
from datetime import date
import turtle
from turtle import *

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
        self.notebook.add(MinigameTab(root), text="Radar")
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
radar_tab = MinigameTab(tab_control)
tab_control.add(terminal_tab, text="Terminal")
tab_control.add(radar_tab, text="Radar")
tab_control.pack(expand=1, fill="both")

# Customization
terminal_tab.config(bg="#000000")
radar_tab.config(bg="#000000")

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
screentext = ["There was no action supplied with that command.\n"
              'Type "Help" for a list of commands.\n'
            ,
            "Welcome to the PERDITUS-26 OS\n"
            "Onboard systems courtesy of Sensus Corporation\n"
            "WARNING: ONBOARD TIME RELATIVITY SYSTEMS OFFLINE\n"
            "\n"
            "Happy " + weekday_greet + ".\n"
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
command_screen = Label(terminal_tab, text=screentext[1], font=("Courier", 12), fg="#00FF00", bg="#000000", anchor=W, justify="left")
entry = Entry(terminal_tab, textvariable=command_var, font=('Courier', 12), fg="#00FF00", bg="#000000")


# Commands
def esc():
    command_screen.config(text=screentext[1])
    entry.delete(0, 'end')

def run():
    command = command_var.get()
    if command == "help" or command == "Help" or command == "HELP":
        help()
    elif command == "route" or command == "Route" or command == "ROUTE":
        route()
    else:
        command_screen.config(text=screentext[0])
    entry.delete(0, 'end')

def help():
    command_screen.config(text=screentext[2])

def route():
    command_screen.config(text=screentext[3])

# TODO make more commands


# TODO make radar screen terminal

# Radar Screen
radar_screen = Canvas(radar_tab, width=282, height=282)

screen = TurtleScreen(radar_screen)
screen.bgcolor("#000000")

# Ship
ship = RawTurtle(screen)
ship.shape("triangle")
ship.setheading(90)

# Draws Radar Graphics
graphics = RawTurtle(screen)
graphics.hideturtle()
graphics.speed(0)

# Draws Radar Animation
STEP = -3
GAP = 337.5
PEN_SIZE = 141
RADIUS = 141

animation = RawTurtle(screen)
animation.speed(0)
animation.backward(RADIUS)
animation.right(90)

# Radar Graphics
def draw_radar():
    spacer = 141
    graphics.pencolor("#2F522A")
    graphics.goto(0, -141)
    graphics.pendown()
    graphics.fillcolor("#2F522A")
    graphics.begin_fill()
    graphics.circle(141)
    graphics.end_fill()
    graphics.pencolor("#56BD3E")
    graphics.goto(0, 141)
    graphics.penup()
    graphics.goto(-141, 0)
    graphics.pendown()
    graphics.goto(141, 0)
    for i in range(1, 5):
        spacer -= 28.2
        graphics.penup()
        graphics.goto(0, -(spacer))
        graphics.pendown()
        graphics.circle(spacer)
    graphics.pencolor("#FFFFFF")

# Radar Animation
def radar_animation():
    def await_loading(degrees=[0], color=["#54AF3C"]):
        animation.color(color)
        animation.tilt(STEP)
        degrees[0] = (degrees[0] + STEP) % 360
        screen.ontimer(await_loading, 10)

    animation.begin_poly()
    animation.circle(RADIUS, 360 - GAP, 60)
    animation.left(90)
    animation.forward(PEN_SIZE)
    # animation.right(90)
    # animation.circle(RADIUS - PEN_SIZE, GAP - 360, 60)
    animation.end_poly()

    screen.addshape('loading', animation.get_poly())

    animation.reset()
    animation.shape('loading')

    await_loading()

draw_radar()

# Grid Packing
def pack():
    command_screen.pack(fill="both")
    entry.pack(fill="both", side=BOTTOM)
    radar_screen.pack(anchor=CENTER)

# Animation Logic
radar_screen.bind("<FocusOut>", radar_animation())

# Bind Keys
entry.bind("<Return>", (lambda event: run()))
entry.bind("<Escape>", (lambda event: esc()))

# Mainloop
pack()
root.mainloop()