from turtle import Turtle


SCORE = "SCORE"
ALIGN = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 275)
        self.write("SCORE: 0", align=ALIGN,font=FONT)
        self.hideturtle()

    def reset_score(self):
        self.score = 0

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(SCORE + ": " + str(self.score), align=ALIGN, font=FONT)