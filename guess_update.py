import turtle
from turtle import Turtle, Screen

class Update_Guess(Turtle):
    def __init__(self):
        super().__init__()
        self.remaining_guess = 10

    def update_guess(self):
        self.clear()
        self.remaining_guess -=1
        self.penup()
        self.goto(-253.0, 439.0)
        self.write(f'{self.remaining_guess} remaining guesses', align='center', font=('Arial', 40, 'bold'))