from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title('snake game ')
screen.bgcolor('black')
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect  collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    for segment1 in snake.segments[1:]:
        if snake.head.distance(segment1)<10:
            scoreboard.reset()
            snake.reset()
            print("you bites yourself")




screen.exitonclick()