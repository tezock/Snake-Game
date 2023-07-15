"""
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")

        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(x=random_x, y=random_y)
"""