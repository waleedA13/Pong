from turtle import Turtle


def game_end(status):
    end_board = Turtle()
    end_board.hideturtle()
    end_board.up()
    end_board.pencolor("red")
    end_board.setposition(-170, 0)
    end_board.write(f"You {status}!!", False, font=("Arial", 70, "normal"))


class ScoreBoard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.up()
        self.pencolor("white")
        self.setposition(x, 360)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, False, font=("Arial", 60, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


