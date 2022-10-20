from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from pygame import mixer

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Nokia's Snake Game")
screen.tracer(0)

# initialization
snake = Snake()
food = Food()
scoreboard = Scoreboard()

mixer.init()
mixer.music.load('music/background-music.mp3')
mixer.music.play()

# Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scores()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
