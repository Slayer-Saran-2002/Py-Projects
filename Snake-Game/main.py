import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
my_screen= Screen()
my_screen.setup(width=600,height=600)
my_screen.title("Python snake game")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
foods=Food()
score_board=ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_on= True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    score_board.refresh()

    # Detect food and show score
    if snake.snake_head.distance(foods)<15:
        score_board.score+=1
        foods.refresh()
        # Increase tail
        snake.extend_tail()

    # Detect wall and tail
    if snake.snake_head.xcor()>280 or snake.snake_head.ycor()>290 or snake.snake_head.xcor()<-280 or snake.snake_head.ycor()<-290:
        game_on=False
        score_board.gameover()

    for body in snake.segments[1:]:
        if snake.snake_head.distance(body)<10:
            game_on = False
            score_board.gameover()






my_screen.exitonclick()

