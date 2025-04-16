from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle') # change shape to circle
        self.penup() # to disallow drawing a line
        self.shapesize(0.5,0.5) # to shrink the size of the circle so to make it smaller than the size of the
        # head of the snake
        self.color('red')
        self.speed('fastest')
        self.move_location()

    def move_location(self):
        random_x = random.randint(-279,279)
        random_y = random.randint(-279,279)
        self.goto(random_x,random_y)