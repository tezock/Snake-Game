from turtle import Turtle



ALIGN = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 275)
        self.high_score = 0
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGN,font=FONT)
        self.hideturtle()


    def reset_score(self):
        self.score = 0

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGN, font=FONT)