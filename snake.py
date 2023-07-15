### Imports ###
import time
from turtle import Turtle, Screen


### Constants ###
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("White")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        

    def move(self):
        segments = self.segments
        
        time.sleep(0.2)
        for segment_number in range(len(segments) - 1, 0, -1):
            new_y = segments[segment_number - 1].ycor()
            new_x = segments[segment_number - 1].xcor()
            segments[segment_number].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
        return

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
        return

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        return

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        return
