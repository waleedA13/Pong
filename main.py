from turtle import Screen, Turtle
from paddle import Paddle
from time import sleep
from scoreboard import ScoreBoard, game_end
from ball import Ball
from random import randint


screen = Screen()
screen.setup(1440, 900, 0, 0)
screen.bgcolor("black")
screen.title("Ping Pong")

# For border of resolution
border = Turtle()
border.hideturtle()
border.speed(0)
border.up()
border.color("white")
border.goto(-720, -450)
border.down()
for i in range(2):
    border.forward(1440)
    border.left(90)
    border.forward(900)
    border.left(90)


# For middle line
middle_Line = Turtle()
middle_Line.hideturtle()
middle_Line.up()
middle_Line.color("white")
middle_Line.speed(0)
middle_Line.goto(0, 440)
middle_Line.setheading(270)
middle_Line.down()
middle_Line.width(7)
for dash in range(32):
    middle_Line.forward(14)
    middle_Line.up()
    middle_Line.forward(14)
    middle_Line.down()


player_paddle = Paddle(-650)
ai_paddle = Paddle(650)


player_scoreboard = ScoreBoard(-100)
ai_scoreboard = ScoreBoard(70)

# Player buttons
screen.tracer(0)
screen.listen()
screen.onkey(player_paddle.up, "Left")
screen.onkey(player_paddle.down, "Right")

ball = Ball()
ball.setheading(180)
game_on = True
while game_on:
    ball.forward(10)
    screen.update()
    sleep(ball.movement_speed)
    ai_paddle.ai_move(ball)

    if ball.ycor() > 430 or ball.ycor() < -430:
        ball.bounce_off(2)

    if ball.distance((720, ball.ycor())) < 10:
        player_scoreboard.add_point()
        ball.reset_position(-60, 60)

    elif ball.distance((-720, ball.ycor())) < 10:
        ai_scoreboard.add_point()
        ball.reset_position(120, 240)

    if (ball.distance(player_paddle) < 50 and ball.xcor() < -625) or (ball.distance(ai_paddle) < 50 and ball.xcor() > 625):
        ball.bouncing += 1
        ball.bounce_off(1)
        ball.movement_speed *= .9
        if ball.bouncing == 2:
            ball.setheading(ball.heading() - 2 ** randint(1, 2))
            ball.bouncing = 0

    if ai_scoreboard.score == 5:
        game_on = False
        game_end("Lose")
    elif player_scoreboard.score == 5:
        game_on = False
        game_end(player_scoreboard.score == 5)

screen.exitonclick()
