from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_gain=10
        self.y_gain=10
        

    def move(self):
        self.goto(self.xcor()+self.x_gain,self.ycor()+self.y_gain)

    def bounce(self):
        self.y_gain *= -1

    def collide(self):
        self.x_gain *= -1

        

        
