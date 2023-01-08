from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.paddle = []
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(90)
        self.goto((x_pos, 0))

    def up(self):
        if self.ycor() != 400:
            self.forward(20)

    def down(self):
        if self.ycor() != -400:
            self.backward(20)

    def ai_move(self, ball):
        if 400 > self.ycor() < ball.ycor():
            self.forward(5)
        elif -400 < self.ycor() > ball.ycor():
            self.backward(5)


