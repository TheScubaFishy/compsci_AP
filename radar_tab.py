# radar_tab.py
from tkinter import *
from turtle import *

class RadarTab(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Customization
        self.config(bg="#000000")

        # Radar Screen
        self.radar_screen = Canvas(self, width=282, height=282)
        self.radar_screen.pack(anchor=CENTER)

        screen = TurtleScreen(self.radar_screen)
        screen.bgcolor("#000000")

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
            def sweep_animation(degrees=[0], color=["#54AF3C"]):
                animation.color(color)
                animation.tilt(STEP)
                degrees[0] = (degrees[0] + STEP) % 360
                screen.ontimer(sweep_animation, 10)

            # Draws Radar
            animation.begin_poly()
            animation.circle(RADIUS, 360 - GAP, 60)
            animation.left(90)
            animation.forward(PEN_SIZE)
            animation.end_poly()

            screen.addshape('radar_sweep', animation.get_poly())

            animation.reset()
            animation.shape('radar_sweep')

            sweep_animation()

        draw_radar()
        radar_animation()

        # Animation Logic
        # self.radar_screen.bind("<Return>", (lambda event: radar_animation()))