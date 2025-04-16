from turtle import Turtle
from food import Food

FONT = ('Courier',40,'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.write(f'Score: {self.score}',align = 'center',font = FONT)

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}',align = 'center',font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def end_game(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game over. Final score: {self.score}',align = 'center',font = FONT)
