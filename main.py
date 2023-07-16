#!/usr/bin/env python
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

### SETUP ### 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        snake.eat()

    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        print("out of bounds") 
    
screen.exitonclick()