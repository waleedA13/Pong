from turtle import Turtle
from random import randint

bouncing = 0


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("hotpink")
        self.penup()
        self.speed(1)
        self.movement_speed = 0.03
        self.bouncing = 0

    def bounce_off(self, ceiling):
        self.setheading(180 * ceiling - self.heading())

    def reset_position(self, beg, end):
        heading = randint(beg, end)
        self.setposition(0, 0)
        self.setheading(heading)
        self.movement_speed = 0.03






