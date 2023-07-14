### Imports ###
import time
from turtle import Turtle


### Constants ###
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("White")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        

    def move(self):
        segments = self.segments
        
        time.sleep(0.1)
        for segment_number in range(len(segments) - 1, 0, -1):
            y = segments[segment_number - 1].ycor()
            x = segments[segment_number - 1].xcor()
            segments[segment_number].goto(x, y)
        segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)
        return

    def down(self):
        self.segments[0].setheading(270)
        return

    def right(self):
        self.segments[0].setheading(0)
        return

    def left(self):
        self.segments[0].setheading(180)
        return
