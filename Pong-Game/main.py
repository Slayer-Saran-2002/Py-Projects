import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

my_screen= Screen()
my_screen.setup(800,600)
my_screen.title("PONG GAME")
my_screen.bgcolor("black")
my_screen.tracer(0)
game_on = True

right_paddle=Paddle((370,0))
left_paddle=Paddle((-370,0))

pong_ball=Ball()

my_screen.listen()
my_screen.onkey(right_paddle.go_up,"Up")
my_screen.onkey(right_paddle.go_down,"Down")
my_screen.onkey(left_paddle.go_up,"w")
my_screen.onkey(left_paddle.go_down,"s")

i=0
while game_on:
    my_screen.update()
    time.sleep(0.1)
    pong_ball.move()
    # Ball bouncing logic
    if pong_ball.ycor()>280 or pong_ball.ycor()<-280:
        pong_ball.bounce()
    if pong_ball.distance(right_paddle)<40 and pong_ball.xcor()>340:
        pong_ball.collide()
    if pong_ball.distance(left_paddle)<40 and pong_ball.xcor()<-340:
        pong_ball.collide()
my_screen.exitonclick()