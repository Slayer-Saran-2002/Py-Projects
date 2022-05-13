from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=('Arial', 15, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over!",align="center",font=('Arial', 15, 'normal'))
        