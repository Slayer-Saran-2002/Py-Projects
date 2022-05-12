from turtle import Turtle
START_POS=[0,-20,-40]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create()
        self.snake_head= self.segments[0]


    def create(self):
        for i in range(0,3):
            snake=Turtle()
            if i == 0:
                snake.shape("arrow")
            else:
                snake.shape('square')
            snake.color("white")
            snake.penup()
            snake.goto(x=START_POS[i],y=0)
            self.segments.append(snake)


    def move(self):
        for index in range(len(self.segments)-1,0,-1):
            new_x= self.segments[index-1].xcor()
            new_y= self.segments[index-1].ycor()
            self.segments[index].goto(new_x,new_y)
        self.snake_head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_head.heading() != 270:
          self.snake_head.setheading(90)
    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)
    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
        