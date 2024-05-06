from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen for arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect if food is eaten between snake and food, *both turtle*
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.update_score()

    # Detect wall collision
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290
            or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_on = False
        scoreboard.game_over()

    # Detect tail Collision, loop thru segments
    for segm in snake.segments[1:]:
        if snake.head.distance(segm) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
