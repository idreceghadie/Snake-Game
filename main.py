from turtle import Screen
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

BOUNDARY = 395
FOOD_COLLISION_DIST = 18
TAIL_COLLISION_DIST = 15

screen = Screen()
screen.setup(800,800)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < FOOD_COLLISION_DIST:
        food.move_location()
        snake.grow()
        score.increase_score()

    if snake.head.xcor() > BOUNDARY or  snake.head.xcor() < -BOUNDARY or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY:
        score.end_game()
        game_is_on = False

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < TAIL_COLLISION_DIST:
            score.end_game()
            game_is_on = False


screen.exitonclick()