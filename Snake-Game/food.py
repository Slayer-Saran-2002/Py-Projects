from turtle import Turtle
import random
class Food(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.1,1.1)
        self.speed("fastest")
        self.penup()
        self.color("magenta")
        self.refresh()
    
    def refresh(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))