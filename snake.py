from turtle import Turtle
from food import Food
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_square = Turtle("square")
            new_square.color('White')
            new_square.penup()
            new_square.goto(pos)
            self.snake_segments.append(new_square) # in order to refer to attribute "snake_segments", use self.

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto((new_x, new_y))
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle("square") # same attributes as the rest of the snake
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position) # position of the last segment
        self.snake_segments.append(new_segment)

    def grow(self):
        # grabs the current position of the last segment of the snake and sends to add_segment method
        self.add_segment(self.snake_segments[-1].position())

